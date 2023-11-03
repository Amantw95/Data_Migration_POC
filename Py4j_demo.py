import subprocess
import time

from py4j.java_gateway import JavaGateway, GatewayParameters

java_class_path = "/Users/aman.sharma/Documents/DemoJavaProject/target/classes:/Users/aman.sharma/opt/miniconda3/share/py4j/py4j0.10.9.7.jar"
specified_port = 25339
java_gateway_process = subprocess.Popen(["java", "-cp", java_class_path, "org.example.JavaGateway", str(specified_port)])

# Wait for the Java Gateway Server to start (you can adjust the sleep time)
time.sleep(5)

# Connect to the Java server
gateway = JavaGateway(gateway_parameters=GatewayParameters(port=specified_port))
# gateway = JavaGateway()
java_object = gateway.entry_point  # This is your MyJavaClass instance

# Call the Java method
result = java_object.add(3, 9)
print("Result of adding 3 and 4 in Java:", result)

gateway.shutdown()


# Commands for Demo:
# lsof -i :25333
#
