#employ driver program
def main():
    work_name = ''
    work_id = ''
    work_shift = 0
    work_pay = 0.0

    #get employee data
    work_name, work_id, work_shift, = get_production_data()

    #create object for production worker class
    worker = emp.ProductionWorker(work_name, work_id, work_shift, work_pay)

    #display production worker data

    print("--------")
    print('name:', worker.get_employ_name())
    print('id:', worker.get_employ_id_num())
    print(
    
