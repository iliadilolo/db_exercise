import PyPDF2


# read the pdf file content
def text_from_pdf(pdf_file):
    text_lines = []

    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()

            lines = text.split('\n')

            for line in lines:
                text_lines.append(line)

    return text_lines


# main part - assign tasks to machines
def assign_tasks(model_data, machines_number):
    model_list = [(model.split(';')[0], int(model.split(';')[1])) for model in model_data]
    sorted_models = sorted(model_list, key=lambda model: model[1], reverse=True)

    tasks_by_machines = [[] for task in range(int(machines_number))]

    for task in sorted_models:
        shortest_machine = min(tasks_by_machines, key=lambda run_time: sum(task[1] for task in run_time))
        shortest_machine.append(task)

    for machine_num, task_list in enumerate(tasks_by_machines, start=1):
        with open(f'machine{machine_num}.task', 'w') as file:
            for test_model in task_list:
                file.write(test_model[0] + '\n')


# pdf file
pdf_file = 'DB exercise.pdf'

# list of models without number of machines
models = text_from_pdf(pdf_file)[:-1]
# number of machines
machines = text_from_pdf(pdf_file)[-1]

# call function
assign_tasks(models, machines)


