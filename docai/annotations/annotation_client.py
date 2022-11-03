import logging
from typing import List, Optional

from docai.annotations.annotations import Annotations
from docai.common.base_client import BaseClient
from docai.common.http_utils import verify_response_or_raise
from docai.generated.api.models import get_model, get_training_document, get_training_documents
from docai.generated.models import ModelTrainingDocumentStatus, PaginatedTrainingDocumentsDto, TrainingDocumentResultDto


class AnnotationClient(BaseClient):
    def _get_training_documents(
        self,
        model_id: str,
        after_id: Optional[str],
        document_status: ModelTrainingDocumentStatus = ModelTrainingDocumentStatus.LABELED,
    ) -> PaginatedTrainingDocumentsDto:
        return verify_response_or_raise(
            get_training_documents.sync_detailed(
                client=self._client, id=model_id, after_id=after_id, document_status=document_status
            )
        )

    def load_annotations(
        self,
        model_id: str,
        load_all_pages: bool = False,
        document_status: ModelTrainingDocumentStatus = ModelTrainingDocumentStatus.LABELED,
    ) -> Annotations:
        """
        Loads annotations from a model using the Butler API
        """
        # First load the model details so the schema can be passed to the Annotations object
        logging.info("Loading model details")
        model_details = verify_response_or_raise(get_model.sync_detailed(client=self._client, id=model_id))

        training_docs_list: List[TrainingDocumentResultDto] = []

        should_fetch_more_docs = True
        after_id = None
        logging.info("Loading training documents")
        while should_fetch_more_docs:
            # Fetch the next batch of training documents
            training_docs_page = self._get_training_documents(model_id, after_id, document_status=document_status)

            # Get details for each training document, which includes the annotations
            for training_doc in training_docs_page.items:
                training_doc_details = verify_response_or_raise(
                    get_training_document.sync_detailed(
                        client=self._client,
                        id=model_id,
                        document_id=training_doc.document_id,
                    ),
                )
                training_docs_list.append(training_doc_details)

            logging.info("Loaded %d of %d training documents", len(training_docs_list), training_docs_page.total_count)

            # Determine if we should fetch more documents
            after_id = training_docs_page.items[-1].document_id
            should_fetch_more_docs = load_all_pages and training_docs_page.has_next

        logging.info("Creating Annotations")
        return Annotations(
            model_details=model_details,
            training_documents=training_docs_list,
        )
