```json
{
    "agent/LongTermMemory.py": {
        "content": "
import logging
from typing import Dict, List
from AgentGPT import StateGraph
from nltk import word_tokenize

class LongTermMemory:
    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initialize LongTermMemory with non-stationary drift index and stochastic regime switch.

        Args:
        - non_stationary_drift_index (float): The index of non-stationary drift in the system.
        - stochastic_regime_switch (bool): Whether the regime switch is stochastic or not.
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch
        self.memory_graph = StateGraph()
        logging.basicConfig(level=logging.INFO)

    def update_memory(self, new_experience: Dict[str, str]) -> None:
        """
        Update the long-term memory with new experience.

        Args:
        - new_experience (Dict[str, str]): The new experience to be added to the memory.

        Returns:
        - None
        """
        try:
            logging.info('Updating memory with new experience')
            self.memory_graph.add_node(new_experience)
        except Exception as e:
            logging.error(f'Error updating memory: {e}')

    def retrieve_memory(self, query: str) -> List[str]:
        """
        Retrieve memory based on the query.

        Args:
        - query (str): The query to retrieve memory.

        Returns:
        - List[str]: The retrieved memory.
        """
        try:
            logging.info('Retrieving memory based on query')
            tokens = word_tokenize(query)
            return self.memory_graph.search_nodes(tokens)
        except Exception as e:
            logging.error(f'Error retrieving memory: {e}')
            return []

    def stochastic_regime_switch_handler(self) -> None:
        """
        Handle stochastic regime switch.

        Returns:
        - None
        """
        try:
            logging.info('Handling stochastic regime switch')
            if self.stochastic_regime_switch:
                self.memory_graph.switch_regime()
        except Exception as e:
            logging.error(f'Error handling stochastic regime switch: {e}')

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    ltm = LongTermMemory(non_stationary_drift_index=0.5, stochastic_regime_switch=True)
    new_experience = {'event': 'launch', 'outcome': 'success'}
    ltm.update_memory(new_experience)
    query = 'What was the outcome of the launch event?'
    retrieved_memory = ltm.retrieve_memory(query)
    print(retrieved_memory)
    ltm.stochastic_regime_switch_handler()
",
        "commit_message": "feat: implement specialized LongTermMemory logic"
    }
}
```