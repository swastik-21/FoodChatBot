import re


def extract_session_id(session_str:str):
    match = re.search(r"/sessions/(.*?)/contexts/",session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""
def get_str_from_food_dict(food_dict: dict):
    return ",".join([f"{int(value) }{key}" for key, value in food_dict.items()])
if __name__ =="__main__":
    print(get_str_from_food_dict({" samosa ": 2," chhole ": 1}))
    # print(extract_session_id("projects/nlp-chatbot-pcbw/locations/global/agent/sessions/90d0ad29-a00d-9957-1b42-8a6ad5ac6216/contexts/ongoing-order"))