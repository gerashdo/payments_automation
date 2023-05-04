from pydantic import BaseModel


class TotalPayments(BaseModel):
    total: float


class DownloadPayments(BaseModel):
    file: bytes
    content_type: str
