from openai_utils import *
from flores200_utils import *
import os
os.environ["OPENAI_API_KEY"] = ""

prompt_temp = 'Please provide the English translation for this sentence. Append the language code at the beginning and separate by a tab. For example, if I give you \"" \
              "language code: swh sentence: Unakuja lini?" \
              you will return -> "swh  When are you coming?". Do not add any other thing apart from the language code provided to you at the beginning and actual translation which follows a tab'
test_dir= 'data/flores200_dataset/devtest'
test_data = load_all_tests(test_dir, 1)
full_contexts = []
for lang_code in test_data.keys():
    data = {"messages": [
        {"role": "user",
         "content": 'language code: '+ lang_code +' sentence: '+ test_data[lang_code][0]}
    ]}
    message = chat_prompt.ChatMessages(messages=[]).from_dict(data)
    full_contexts.append(message)

prompt_template = chat_prompt.ChatMessages(messages=[chat_prompt.ChatTurn(role="user", content=prompt_temp)])
lm_conf = lm_config.LMConfig("openai", "gpt-3.5-turbo")

async def gen():
    responses = await generate_from_openai_chat_completion(
        full_contexts = full_contexts,
        prompt_template = prompt_template,
        model_config = lm_conf,
        temperature=0.1, max_tokens=400, top_p=1,
        context_length= -1
    )
    f = open("flores_1_liner.en", "w")
    for line in responses:
        f.write(line+"\n")
    f.close()

    print(responses)

asyncio.run(gen())