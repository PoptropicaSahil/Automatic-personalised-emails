import yagmail
from dotenv import load_dotenv
import os
import pandas as pd
import shutil
from openai_call import personalised_sentence
import logging
from config import CONFIG

load_dotenv()

logging.basicConfig(
    filename="runs.log",
    filemode="a",  # 'a' for append mode, 'w' for overwrite
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

EMAIL_ID = os.getenv(key="EMAIL_ID")
APP_PASSWORD = os.getenv(key="APP_PASSWORD")

CONTACTS_FILE_PATH = CONFIG.CONTACTS_FILE_PATH
BASE_RESUME_PATH = CONFIG.BASE_RESUME_PATH

# Initialize
yag = yagmail.SMTP(user=EMAIL_ID, password=APP_PASSWORD)


def send_email(
    recipient_name,
    company_name,
    company_domain=None,
    company_suffix=None,
):
    # Generate email address

    # Some companies like American Express have domain as aexp
    company_domain = company_name if pd.isna(company_domain) else company_domain
    company_domain = str(company_domain).lower()

    # handle cases when domain has numbers (like 247) and pandas treats as 247.0
    if company_domain.endswith(".0"):
        company_domain = company_domain[:-2]

    # Similarly for suffix
    company_suffix = "com" if pd.isna(company_suffix) else company_suffix
    company_suffix = str(company_suffix).lower()

    try:
        first_name = recipient_name.split()[0]
        last_name = recipient_name.split()[1]
        recipient_email = f"{first_name.lower()}.{last_name.lower()}@{company_domain}.{company_suffix}"

    except IndexError:
        logging.warning(
            "Only single name provided, trying to send but highly likely it may not work... "
        )
        first_name = recipient_name.split()[0]
        recipient_email = f"{first_name.lower()}@{company_domain}.{company_suffix}"

    recipient_email = "loramolly093@gmail.com"

    logging.info(f"Checking email to: {recipient_email}")

    openai_sentence = personalised_sentence(company_name=company_name).strip()

    subject = CONFIG.subject.format(company_name=company_name)
    body = CONFIG.body.format(
        first_name=first_name,
        company_name=company_name,
        openai_sentence=openai_sentence,
    )

    # Copy and rename resume file
    resume_filename = f"./resumes/Sahil_Resume_DataScience_{company_name}.pdf"
    shutil.copy(src=BASE_RESUME_PATH, dst=resume_filename)

    # Send email
    yag.send(
        to=recipient_email, subject=subject, contents=body, attachments=resume_filename
    )

    # Remove the generated resume file
    os.remove(resume_filename)

    return recipient_email


def main():
    # Load Contacts
    df = pd.read_excel(CONTACTS_FILE_PATH)

    # Filter DataFrame
    # Not doing this becuase it overwrote the original dataframe
    # df = df[df["Sent_Indicator"].str.strip().str.lower() != "yes"]

    # Iterate through DataFrame and send emails if not sent
    for index, row in df.iterrows():
        logging.info(
            f'Index={index}, checking row from data: {row["Name"]} at {row["Company"]}...'
        )

        if row["Sent_Indicator"].strip().lower() != "yes":
            try:
                recipient_email = send_email(
                    recipient_name=row["Name"],
                    company_name=row["Company"],
                    company_domain=row["mail_domain"],
                    company_suffix=row["mail_suffix"],
                )

                # Update DataFrame
                df.at[index, "Sent_Indicator"] = "Yes"
                logging.info(f"\t Email sent to: {recipient_email}")

            except Exception as e:
                logging.info(f"\t Failed to send email to {row['Name']}: {e}")

    # Save updated DataFrame back to Excel
    df.to_excel(
        excel_writer=CONTACTS_FILE_PATH,
        index=False,
    )


if __name__ == "__main__":
    main()
