import json

from typing import List
from dataclasses import dataclass

from xendit._api_requestor import _APIRequestor
from xendit._extract_params import _extract_params

from xendit.xendit_error import XenditError

from .invoice_bank import InvoiceBank


@dataclass
class Invoice:
    """Invoice class (API Reference: Invoice)

    Related Classes:
      - InvoiceBank

    Static Methods:
      - Invoice.create (API Reference: /Create Invoices)

    Attributes:
      - id (str)
      - external_id (str)
      - user_id (str)
      - status (str)
      - merchant_name (str)
      - merchant_profile_picture_url (str)
      - amount (int)
      - payer_email (str)
      - description (str)
      - expiry_date (str)
      - invoice_url (str)
      - available_banks (InvoiceBank[])
      - available_ewallets (?)
      - should_exclude_credit_card (bool)
      - should_send_email (bool)
      - created (str)
      - updated (str)
      - currency (str)

    """

    id: str
    external_id: str
    user_id: str
    status: str
    merchant_name: str
    merchant_profile_picture_url: str
    amount: int
    payer_email: str
    description: str
    invoice_url: str
    expiry_date: str
    available_banks: List[InvoiceBank]
    available_ewallets: List[None]
    should_exclude_credit_card: bool
    should_send_email: bool
    created: str
    updated: str
    currency: str

    def __repr__(self):
        return json.dumps(vars(self), indent=4)

    @staticmethod
    def create(
        *,
        external_id,
        payer_email,
        description,
        amount,
        should_send_email=None,
        callback_virtual_account_id=None,
        invoice_duration=None,
        success_redirect_url=None,
        failure_redirect_url=None,
        payment_methods=None,
        mid_label=None,
        currency=None,
        fixed_va=None,
        reminder_time=None,
        for_user_id=None,
        x_idempotency_key=None,
        x_api_version=None,
        **kwargs,
    ):
        """Send POST Request to create Invoice (API Reference: Invoice/Create Invoice)

        Args:
          - external_id (str)
          - payer_email (str)
          - description (str)
          - amount (int)
          - **should_send_email (bool)
          - **callback_virtual_account_id (str)
          - **invoice_duration (int)
          - **success_redirect_url (str)
          - **failure_redirect_url (str)
          - **payment_methods (str[])
          - **mid_label (str)
          - **currency (str)
          - **fixed_va (bool)
          - **reminder_time (int)
          - **for_user_id (str) (XenPlatforms only)
          - **x_idempotency_key (str)
          - **x_api_version (str): API Version that will be used. If not provided will default to the latest

        Returns:
          Invoice

        Raises:
          XenditError

        """
        url = "/v2/invoices"
        headers, body = _extract_params(
            locals(),
            func_object=Invoice.create,
            headers_params=["for_user_id", "x_idempotency_key", "x_api_version"],
        )
        kwargs["headers"] = headers
        kwargs["body"] = body

        resp = _APIRequestor.post(url, **kwargs)
        if resp.status_code >= 200 and resp.status_code < 300:
            return Invoice(**resp.body)
        else:
            raise XenditError(resp)
