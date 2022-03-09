echo -n "Insert the server folder name: ";
read;
python3 clone_server.py $(REPLY)
cd $(REPLY)

sh ../commit_server.sh
sh ../push_server.sh
sh ../pull_server.sh

sh start.sh