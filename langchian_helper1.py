from langchain.prompts import PromptTemplate

from langchain.llms import GooglePalm

api = "AIzaSyCE8GPxkKGibdVtSpL4SooR_7hS7auBzWI"
llm = GooglePalm(google_api_key=api, temperature=0)


def generate_details(source,destination,date):
    prompt_template_places_date = PromptTemplate(
        input_variables=['source', 'destination', 'date'],
        template="Flights from {source} to {destination} for {date} create a table with add another column before it with airplane company name first column flight name second departure time third landing time fourth if any layover then what time is the layover and another column of the layover destination and the another being the date and the last being the cost of the flight also add landing date ",
    )



    from langchain.chains import LLMChain

    model = LLMChain(llm=llm, prompt=prompt_template_places_date)
    response=model.run({'source':source,'destination':destination,'date':date})

    return response

if __name__=='__main__':
    print(generate_details("mumbai","delhi","2023-11-11"))