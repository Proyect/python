from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import os 

driver = webdriver.Chrome()

driver.get("https://sge.salta.gob.ar/ui/#!/login")
driver.implicitly_wait(0.5)
input("presione luego de carga login")
input_element = driver.find_element(By.ID, value="login-usuario")
input_element.send_keys("")
input_element = driver.find_element(By.ID, value="login-contrasenia")
input_element.send_keys("")
button_element = driver.find_element(By.ID, value="login-btn")
button_element.click()
print("Done Login.")
print("Start Data Enter Process")
time.sleep(5)
listNoCUIL = [] 
listNoFind = []
time.sleep(5)
os.system("cls")
# Abre el archivo CSV
with open("list.csv", "r") as f:
    lector = csv.reader(f)
    print("Start data enter")
    for element in lector:
        print("Data to analize: ")
        element = element[0].split(";")
        #print(element)
        if(len(element[3])==11):# correct cuil 
            print("Seach to correct Data: " + element[2] +", " +element[1] + "  "+ element[3])
            driver.get("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/search///")
            print("Ingresando a https://sge.salta.gob.ar/ui/#!/home/unidad/18239/search///")
            input("si cargo el site, presione enter")                        
            input_element = driver.find_element(By.ID, value="persona-busqueda-input")
            input_element.send_keys(element[3])    
            button_element = driver.find_element(By.ID, value="persona-busqueda-buscar")
            button_element.click()
            ops = input("Ingrese: 1: si existe en la carga. 2: si requiere carga manual")
            if(ops =="1"):
                searchText = driver.find_element(By.CLASS_NAME, value="clickable")
                searchText.click()
            else:
                driver.get("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/usuario/ ")
                print("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/usuario/ ")
                input("Presione enter cuando cargue el site")
                
                input_element = driver.find_element(By.ID, value="apellido")
                input_element.send_keys(element[1])

                input_element = driver.find_element(By.ID, value="nombre")
                input_element.send_keys(element[2])

                input_element = driver.find_element(By.XPATH, '//*[@id="tipo_documento"]/input[1]')
                input_element.send_keys("DNI")

                input_element = driver.find_element(By.ID, value="nro_documento")
                input_element.send_keys(element[12])

                input_element = driver.find_element(By.ID, value="cuil")
                input_element.send_keys(element[3])

                input_element = driver.find_element(By.NAME, value="fechaNacimientoInput")
                input_element.send_keys(element[4])

                input_element = driver.find_element(By.NAME, value="email")
                input_element.send_keys(element[11])

                input_element = driver.find_element(By.NAME, value="password")
                input_element.send_keys("SGE"+element[3])

                input_element = driver.find_element(By.NAME, value="confirmation_password")
                input_element.send_keys("SGE"+element[3])

                input("esperando")

            # carga de materias
            print("Ingresando: https://sge.salta.gob.ar/ui/#!/home/unidad/18239/roles-gestion/"+element[3])
            driver.get("https://sge.salta.gob.ar/ui/#!/home/unidad/18239/roles-gestion/"+element[3])
            time.sleep(5)
            input("pRESIONE ENTER SI SE CARGO EL SITIO")
            text_element = driver.find_element(By.XPATH, '//*[@id="page-content"]/div/div/div/roles-seleccion/div[2]/div[5]/sge-card/div/div/card-header/span')
            text_element.click()
            input("ingrese enter al terminar la carga del site")
            button_element = driver.find_element(By.XPATH,'//*[@id="page-content"]/div/div/div/roles-seccion-curricular/sge-select-lists/div[2]/div[1]/div[2]/ul/li[1]/a')
            button_element.click()

            button_element = driver.find_element(By.XPATH, '//*[@id="page-content"]/div/div/div/roles-seccion-curricular/sge-select-lists/div[2]/div[2]/div/button[1]/span')
            button_element.click()
            
            button_element = driver.find_element(By.XPATH, '//*[@id="page-content"]/div/div/div/roles-seccion-curricular/form-buttons/div/button/span')
            button_element.click()
            input("Siguiente Elemento ?")
        else: #bad Cuil
            listNoCUIL.append(element)
            print("Cuil No correct")
input("press to End")    
    



##driver.quit() SGE + cuil