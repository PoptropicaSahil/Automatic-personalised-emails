class PROMPTS:
    user_prompt = "Company name: {company_name}"

    system_prompt_task = """
    You are a helpful smart assistant that has knowledge about many companies, their work, their products, and applications in data science. 
    I am writing mails to recruiters and your task is that - given a company's name by the user, you have to relate my background information with the company's working and give me TWO and only TWO crisp statements about how I can be impactful for this company.
    Your two-sentence response should be very specific, and it should take information from my at Walmart, research in AI, impact-driven work AND very specific and niche information about what the company does. The focus should be on the company's work, products, vision, need for Data Science and shift towards AI, and how I can impact them.
    If the company's name is empty, write generically about company's growing interest in AI
    Avoid using words like expertise, instead use experience or great interest. 
    Your response should begin with - 'I belive my work <fill here> can be impactful to your team at <company name>.'
    Strictly DO NOT return anything else. Response should not cross 30 words.
    """

    system_prompt_sahil_background = """
    Here is my information in detail:
    Sahil Girhepuje is a highly accomplished data science professional with a strong academic background and extensive industry experience. He graduated with a Dual Degree (BTech + MTech) in Engineering Design and Data Science from the prestigious Indian Institute of Technology Madras (IITM), achieving a remarkable CGPA of 9.22/10. Sahil’s academic excellence has been recognized with numerous awards, including the Shankar Family & Venkitaramanan scholarship and the Ms. Latha & Sampath Srinath Prize for the highest CGPA in his second year.

    In terms of professional experience, Sahil has worked at leading companies like Walmart Global Tech, American Express, and Securin.io, where he utilized various tools and technologies to create impactful data-driven solutions. At Walmart Global Tech, he used SAP to manage the my-GNFR tool, handling $68 billion in indirect spending across 89,000 associates. During his Analytics Internship at American Express, he worked with SQL to analyze 2.2 million customer calls over dynamic time periods and proposed a novel profitability metric, potentially saving $1 million. His Data Science Internship at Walmart Global Tech further involved Dask and MLflow to develop a no-code time-series forecasting framework expected to save $111 million.
    At Securin.io, Sahil was involved in cybersecurity projects where he utilized Python, AI Bill of Materials frameworks, and cybersecurity protocols like MITRE ATT&CK and OWASP Top-10 risks to propose AI-driven solutions. His proficiency extends to working with large-scale datasets, having analyzed over 77 billion records using Google BigQuery.
    In addition to these tools, Sahil has demonstrated leadership by overseeing the development of several projects, including models from scratch for LLM and Stable Diffusion, showcasing his technical expertise in coding complex machine learning models using frameworks such as Docker, FastAPI, and Apache Airflow. He is also proficient with cloud platforms like Google Cloud and AWS, making him highly adept at managing large-scale data workflows and deployments.

    Sahil has also contributed significantly to academia, authoring several research papers on topics like offensive AI, adversarial machine learning, and bias in language models. His research work at the Centre for Responsible AI (CeRAI) and RBCDSAI at IITM involved proposing a Legal Safety Score for LLMs, which greatly improved the safety and fairness metrics of models such as LLaMA and LLaMA-2.
    He has worked extensively with machine learning frameworks, building entire models from scratch, including LLaMA2-7B and Stable Diffusion, showcasing his technical proficiency in areas like attention mechanisms, inferencing, and neural networks. He also demonstrated leadership as a team lead in various InterIIT Tech Meet competitions, securing top positions by developing innovative AI and machine learning tools.
    His technical expertise spans various frameworks and tools such as Docker, FastAPI, Apache Airflow, Google Cloud, AWS, and more, making him well-versed in modern software engineering and data science practices.        
    """
