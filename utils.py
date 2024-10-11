from pathlib import Path


def create_resume_filename(resume_path, company_name):
    # Convert the resume path to a Path object
    resume_path = Path(resume_path)

    # Replace spaces in the company name with underscores
    company_name = company_name.replace(" ", "_")

    # Create the new filename by appending the company name before the file extension
    new_resume_filename = resume_path.with_stem(f"{resume_path.stem}_{company_name}")

    return new_resume_filename
