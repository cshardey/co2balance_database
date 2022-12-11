# PostgreSQL Streaming Replication With Docker

The *.txt files here hold user and database parameters. Specifically, `replication.txt` contains the user/role and password to use for replication. Whereas `database.txt` contains an initial database, user/role and password to create on the master.

Run the master:

    $ fig run -d master

Wait for it to start up completely. Start the slave:

    $ fig run slave

Wa-la!
