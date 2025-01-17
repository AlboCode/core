from cat.memory.vector_memory import VectorMemory


# This class represents the Cat long term memory (content the cat saves on disk).
class LongTermMemory:
    """Cat's non-volatile memory.

    This is an abstract class to interface with the Cat's vector memory collections.

    Attributes
    ----------
    vectors : VectorMemory
        Vector Memory collection.
    """

    def __init__(self, ):
        # Vector based memory (will store embeddings and their metadata)
        self.vectors = VectorMemory()


    async def init_memory_config(self, vector_memory_config={}):
        """Initializes the memory configuration.

        Parameters
        ----------
        vector_memory_config : dict, optional
            Configuration for the vector memory, by default {}.
        """
        # Initialize vector memory
        await self.vectors.init_collections(vector_memory_config)


        # What type of memory is coming next?
        # Surprise surprise, my dear!