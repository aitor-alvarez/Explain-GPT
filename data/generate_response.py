from data.data_sources import get_top_headlines
from models.openAI import get_completion_response


def generate_prompts(num_headlines=3):
    instruction =  "Could you explain the following headline based on existing evidence and available knowledge: "
    headlines = get_top_headlines(k_top=num_headlines)
    instructions = [instruction+ h for h in headlines]
    prompts = [{"role": "system", "content":i} for i in instructions]
    return prompts, headlines


def generate_explanations():
    prompts, headlines = generate_prompts()
    for j in range(0, len(prompts)):
        explanation = get_completion_response([prompts[j]])
        txt = explanation['choices'][0]['message']['content']
        print(f'My opinion and explanation of { headlines[j] }: { txt }')
    return None



