import sys
from typing import Callable, Dict, List

import evaluate
import numpy as np
from transformers import EvalPrediction

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

SPECIAL_TOKEN = -100


def generate_layoutlm_compute_eval_metric_fn(
    ner_labels: List[str],
    metric_name: Literal["seqeval"],
    return_entity_level_metrics: bool = False,
) -> Callable[[EvalPrediction], Dict]:
    """
    Generate a function that computes evaluation metrics for a LayoutLM model.

    Args:
        ner_labels: The list of NER labels
        metric_name: The name of the metric to use. Currently only supports "seqeval"
        return_entity_level_metrics: Whether to return entity level metrics as well as overall metrics
    """

    metric = evaluate.load(metric_name)

    def compute_eval_metrics(
        p: EvalPrediction,
    ) -> Dict:
        """
        Compute eval metrics for use when training a LayoutLM model.
        Can be used as the `compute_metrics` argument to `Trainer`.

        Args:
            p: The eval predictions and labels from the model
        """
        predictions, labels = p
        predictions = np.argmax(predictions, axis=2)

        # Filter out special tokens
        true_predictions = [
            [ner_labels[p] for (p, l) in zip(prediction, label) if l != SPECIAL_TOKEN]
            for prediction, label in zip(predictions, labels)
        ]
        true_labels = [
            [ner_labels[l] for (_, l) in zip(prediction, label) if l != SPECIAL_TOKEN]
            for prediction, label in zip(predictions, labels)
        ]

        results = metric.compute(predictions=true_predictions, references=true_labels)

        # If we want entity level metrics, unpack the nested dictionaries
        if return_entity_level_metrics:
            # Unpack nested dictionaries
            final_results = {}
            for key, value in results.items():
                if isinstance(value, dict):
                    for n, v in value.items():
                        final_results[f"{key}_{n}"] = v
                else:
                    final_results[key] = value
            return final_results
        # Otherwise, only return the overall metrics
        else:
            return {
                "precision": results["overall_precision"],
                "recall": results["overall_recall"],
                "f1": results["overall_f1"],
                "accuracy": results["overall_accuracy"],
            }

    return compute_eval_metrics
