import gradio as gr
from chat_ppt_agent import ChatPPTAgent

# from utils.logger import LOG

# 实现对话 Agent 和场景 Agent 的选择与调用
chatppt_agent = ChatPPTAgent()


# 对话 Agent 处理函数
def handle_conversation(user_input, chat_history):
    # LOG.debug(f"[聊天记录]: {chat_history}")
    # bot_message = conversation_agent.chat(user_input)
    bot_message = chatppt_agent.chat_with_history(user_input)
    # LOG.info(f"[ChatBot]: {bot_message}")
    return bot_message


# 场景 Agent 处理函数，根据选择的场景调用相应的 Agent
def handle_scenario(user_input, history, scenario):
    agents = {"PPT生成": chatppt_agent}
    return agents[scenario].respond(user_input)


# Gradio 界面
with gr.Blocks(title="PPT生成") as language_mentor_app:
    with gr.Tab("PPT生成"):
        gr.Markdown("## PPT生成 ")
        conversation_chatbot = gr.Chatbot(
            placeholder="<strong>PPT生成</strong>",
            height=800,
        )

        gr.ChatInterface(
            fn=handle_conversation,
            chatbot=conversation_chatbot,
            retry_btn=None,
            undo_btn=None,
            clear_btn="清除历史记录",
            submit_btn="发送",
        )


if __name__ == "__main__":
    language_mentor_app.launch(server_name="127.0.0.1")
