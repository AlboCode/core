from typing import List
from abc import ABC, abstractmethod

from langchain_core.utils import get_colored_text

from cat.utils import BaseModelDict
from cat.log import log

class AgentOutput(BaseModelDict):
    output: str
    intermediate_steps: List = []
    return_direct: bool = False


class BaseAgent(ABC):

    @abstractmethod
    async def execute(*args, **kwargs) -> AgentOutput:
        pass

    # TODO: this is here to debug langchain, take it away
    def _log_prompt(self, langchain_prompt, title):
        print("\n")
        print(get_colored_text(f"==================== {title} ====================", "green"))
        for m in langchain_prompt.messages:
            print(get_colored_text(type(m).__name__, "green"))
            print(m.content)
        print(get_colored_text(f"========================================", "green"))
        return langchain_prompt
    
    # TODO: this is here to debug langchain, take it away
    def _log_output(self, langchain_output, title):
        print("\n")
        print(get_colored_text(f"==================== {title} ====================", "blue"))
        print(langchain_output.content)
        print(get_colored_text(f"========================================", "blue"))
        return langchain_output