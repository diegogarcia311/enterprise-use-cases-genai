from langchain.memory import ConversationBufferMemory

class CustomMemory(ConversationBufferMemory):
    def save_context(self, inputs, outputs):
        super().save_context(inputs, outputs)
        print(f"[Memory] {inputs['input']} -> {outputs['output']}")
