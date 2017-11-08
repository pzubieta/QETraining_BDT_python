import logging
import logging.config

#FUNCTION TO CALCULATE THE SALES SALARY RECEIVING THE NUMBER OF PIECES SOLD AS ARGUMENT
def calc_total_sales_salary(pieces_sold):
    p_sold=float(pieces_sold)
    sales_salary=float(p_sold*2.5)
    return sales_salary

#FUNCTION TO CALCULATE THE FACTORY SALARY RECEIVING THE NUMBER OF EFFECTIVE PIECES AND DEFECTIVE PIECES
def calc_total_factory_salary(total_pieces, defective_pieces):
    d_pieces=float(defective_pieces)*1.3
    t_pieces=float(total_pieces*10)
    factory_salary=t_pieces - d_pieces

    #Displaying the number of pieces since looks like a important information
    print ("The number of total pieces is: ",total_pieces)
    print("The number of defective pieces is: ", defective_pieces)
    return factory_salary

#FUNCTION TO CALCULATE THE DISCOUNT RECEIVING THE VALUE OF ANY SALARY
def calc_discount_salary(any_salary):
    discount_salary=any_salary*0.125
    return discount_salary

