gen_proto:
	python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ --proto_path=../protos udaconnect.proto

docker_build:
	docker build -t tpso/udaconnect-core .

docker_push:
	docker push tpso/udaconnect-core