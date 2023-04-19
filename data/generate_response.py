from data.data_sources import get_top_headlines
from models.openAI import get_completion_response


def generate_prompts(num_headlines=3):
    instruction =  "Provide a factual opinion on the following news headline: "
    headlines = get_top_headlines(k=num_headlines)
    instructions = [instruction+ h for h in headlines]
    prompts = [{"role": "system", "content":i} for i in instructions]
    return prompts, headlines


def generate_opinion():
    prompts, headlines = generate_prompts()
    for j in range(0, len(prompts)):
        opinion = get_completion_response(prompts[j])
        print(f'My opinion on { headlines[j] }: { opinion }')
    return None



