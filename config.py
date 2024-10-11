class CONFIG:
    # Ensure that the following paths are correct
    CONTACTS_FILE_PATH = "./contacts/contacts-sample.xlsx"
    BASE_RESUME_PATH = "./resumes/jakes-resume.pdf"

    # Model from OpenRouter to use for personlisation
    model_name = "google/gemini-flash-1.5-8b"

    # Email Subject
    subject = "Walmart, IIT Madras Data Scientist for {company_name}"

    # Email Body
    # It is perfectly possible to have a usual text body. But using HTML tags allow for more customization!
    body = """Hi {first_name}, came across your profile on LinkedIn.
    I'm an IITM graduate at Walmart, and I've authored 5 research papers in Data Science - including <strong>LLMs</strong>. I really admire the innovative work at {company_name}, especially applications in Data Science and Analytics; would love to explore positions in your team. Please find my resume attached.
    
    Here are a few highlights from my resume:
    <ul style="margin: 0; padding: 0; list-style-position: inside;">
        <li style="margin: 0; padding: 0; line-height: 1.2;"><strong>CGPA 9.22</strong> (highest!) from IIT Madras, BTech+MTech in Engineering Design and Data Science. 5 research papers live <a href="https://scholar.google.com/citations?user=bAR0zX8AAAAJ&hl=en">link</a></li>
        <li style="margin: 0; padding: 0; line-height: 1.2;">Spent <strong>20 months</strong> at <strong>Walmart Global Tech, American Express</strong>, and Securin.io</li>
        <li style="margin: 0; padding: 0; line-height: 1.2;"><strong>Led</strong> the 8-member IITM AI team at the 12th Inter-IIT Tech Meet</li>
    </ul>
    {openai_sentence} Looking forward to hearing from you!

    Sahil Girhepuje <a href="https://www.linkedin.com/in/sahil-girhepuje/">[LinkedIn]</a>
    """
