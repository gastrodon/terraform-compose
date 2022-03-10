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

    migrate_state: bool = Field(False, alias="no-backend")
    reconfigure: bool = False
    get_modules: bool = Field(True, alias="no-get-modules")
    lock: bool = Field(True, alias="no-lock")
    input: bool = Field(False, alias="no-input")
    backend: bool = Field(True, alias="no-backend")
    backend_config: List[str] = Field([], alias="backend-config")
