
import pandas as pd
data_folder = "../data/"


def get_train():
    train = pd.read_csv(data_folder + "Entrenamieto_ECI_2020.csv", dtype={"ID": "int16",
                                                                          "Region": "category",
                                                                          "Territory": "category",
                                                                          "Pricing, Delivery_Terms_Quote_Appr": "int16",
                                                                          "Pricing, Delivery_Terms_Approved": "int16",
                                                                          "Bureaucratic_Code_0_Approval": "category",
                                                                          "Bureaucratic_Code_0_Approved": "category",
                                                                          "Submitted_for_Approval": "int16",
                                                                          "Bureaucratic_Code": "category",
                                                                          "Source": "category",
                                                                          "Billing_Country": "category",
                                                                          "Account_Owner": "category",
                                                                          "Opportunity_Owner": "category",
                                                                          "Account_Type": "category",
                                                                          "Opportunity_Type": "category",
                                                                          "Quote_Type": "category",
                                                                          "Delivery_Terms": "category",
                                                                          "Brand": "category",
                                                                          "Product_Type": "category",
                                                                          "Size": "category",
                                                                          "Product_Category_B": "category",
                                                                          "Price": "category",
                                                                          "Currency": "category",
                                                                          "ASP_Currency": "category",
                                                                          "Delivery_Quarter": "category",
                                                                          "Total_Amount_Currency": "category",
                                                                          "Total_Taxable_Amount_Currency": "category",
                                                                          "Delivery_Year": "int16",
                                                                          "Stage": "object",
                                                                          "Prod_Category_A": "category",
                                                                          "Product_Family": "category",
                                                                          "Product Name": "category",
                                                                          })

    train["Planned_Delivery_End_Date"] = pd.to_datetime(train["Planned_Delivery_End_Date"], infer_datetime_format=False,
                                                        errors="coerce")
    train["Planned_Delivery_Start_Date"] = pd.to_datetime(train["Planned_Delivery_Start_Date"],
                                                          infer_datetime_format=False, errors="coerce")
    train["Last_Modified_Date"] = pd.to_datetime(train["Last_Modified_Date"], infer_datetime_format=False,
                                                 errors="coerce")
    train["Opportunity_Created_Date"] = pd.to_datetime(train["Opportunity_Created_Date"], infer_datetime_format=False,
                                                       errors="coerce")
    train["Account_Created_Date"] = pd.to_datetime(train["Account_Created_Date"], infer_datetime_format=False,
                                                   errors="coerce")
    train["Month"] = pd.to_datetime(train["Month"], infer_datetime_format=False, errors="coerce")
    # Elimino las columnas con un solo valor
    del train['Submitted_for_Approval']
    del train['Last_Activity']
    del train['ASP_(converted)_Currency']
    del train['Actual_Delivery_Date']
    del train['Prod_Category_A']
    return train
