# path-based-mac
A repo for ideas on a Path based MAC or lateral movement detection tool built on a graphdb.

* Make decisions about access control with the full context of what a "user" has accessed during a "login session" ("user path")
* Designate "controlled entrypoints" for "user login"
* Deny or detect as anomoly when a "user path" begins not from a "controlled entrypoint" or otherwise cannot be connected to an existing "user path"
* Use a graph to track "user paths", compare against historic data historic "login sessions"

Will transcribe notes later, picture of whiteboard for now.
