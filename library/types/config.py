from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Config(BaseModel):
    path: str = "."
    no_destroy: bool = Field(False, alias="no-destroy")

    input: bool = False
    lock: bool = False
    parallelism: int = 10
    state: Optional[str] = Field(None, alias="state-state")
    state_backup: Optional[str] = Field(None, alias="state-backup")
    state_out: Optional[str] = Field(None, alias="state-out")

    refresh: bool = False
    refresh_only: bool = Field(None, alias="refresh-only")
    replace: List[str] = []
    target: List[str] = []
    var: Dict[str, Any] = {}
    var_file: List[str] = Field([], alias="var-file")

    no_backend: bool = Field(False, alias="no-backend")
    no_get_modules: bool = Field(False, alias="no-get-modules")
    no_lock: bool = Field(False, alias="no-lock")
    no_input: bool = Field(True, alias="no-input")
    backend_config: List[str] = Field([], alias="backend-config")
