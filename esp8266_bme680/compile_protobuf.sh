brew install protobuf
pip3 install protobuf grpcio-tools
python3 /Users/gerold/IoTProject/nanopb/generator/nanopb_generator.py *.proto 
protoc --python_out=. *.proto