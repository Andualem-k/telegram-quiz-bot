# cs_questions.py

CS_EXIT_EXAM_2018 = [
    {
        "id": 1,
        "question": "nav ul {\n  list-style-type: none;\n  margin: 0;\n  padding: 0;\n}\nWhat problem does this solve when creating a navigation bar?",
        "options": [
            "Removes bullet points and default spacing, allowing custom layout",
            "Aligns the navbar to the right of the page",
            "Adds hover effects to list items",
            "Converts the list into a dropdown menu"
        ],
        "correct_answer": "Removes bullet points and default spacing, allowing custom layout",
        "explanation": "Setting list-style-type to none removes bullet points, while setting margin and padding to 0 removes default browser spacing."
    },
    {
        "id": 2,
        "question": "Which AI approach most directly supports understanding biological intelligence behavior as a scientific goal?",
        "options": ["Weak AI", "Applied AI", "Cognitive AI", "Strong AI"],
        "correct_answer": "Cognitive AI",
        "explanation": "Cognitive AI focuses on modeling biological intelligence and cognitive behavior."
    },
    {
        "id": 3,
        "question": "In client-server database architecture, what is the primary role of the server?",
        "options": [
            "Provide the GUI for end users",
            "Initiate all network connections and poll clients for updates",
            "Store and manage shared data, enforce ACID properties, and process client requests",
            "Cache all user sessions locally for offline access"
        ],
        "correct_answer": "Store and manage shared data, enforce ACID properties, and process client requests",
        "explanation": "The primary role of the database server is storing shared data and handling requests."
    },
    {
        "id": 4,
        "question": "Which automaton is powerful enough to recognize the language L = {aⁿbⁿcⁿ | n ≥ 1}?",
        "options": ["DFA", "Linear Bounded Automaton (LBA)", "NFA", "Pushdown Automaton (PDA)"],
        "correct_answer": "Linear Bounded Automaton (LBA)",
        "explanation": "Context-sensitive languages like L={aⁿbⁿcⁿ} are recognized by Linear Bounded Automata."
    },
    {
        "id": 5,
        "question": "In two-phase locking (2PL), during which phase may a transaction acquire locks but not release any?",
        "options": ["Growing phase", "Commit phase", "Validation phase", "Shrinking phase"],
        "correct_answer": "Growing phase",
        "explanation": "In 2PL, locks are acquired during the growing phase."
    },
    {
        "id": 6,
        "question": "To extend the connectivity of processor bus we use:",
        "options": ["SCSI", "PCI", "Controllers", "Multi bus"],
        "correct_answer": "Multi bus",
        "explanation": "Multi bus systems extend processor bus connectivity."
    },
    {
        "id": 7,
        "question": "Combinational circuit differ from sequential circuit primarily because",
        "options": [
            "Combinational circuit cannot be built using logic circuit",
            "The output of combinational circuit depends only on the present input, not on past output.",
            "Sequential circuit have no feedback while combinational circuit do",
            "The combinational circuit requires clock signal, but sequential circuit do not"
        ],
        "correct_answer": "The output of combinational circuit depends only on the present input, not on past output.",
        "explanation": "Combinational circuits rely only on present inputs."
    },
    {
        "id": 8,
        "question": "Why is Greedy Best-First Search not guaranteed to be optimal or complete?",
        "options": [
            "It ignores path cost g( n) and relies only on h( n)",
            "It always chooses the shallowest node",
            "It expands nodes in FIFO order",
            "It requires full knowledge of the goal state in advance"
        ],
        "correct_answer": "It ignores path cost g( n) and relies only on h( n)",
        "explanation": "Greedy Best-First Search ignores actual path cost g(n)."
    },
    {
        "id": 9,
        "question": "From the following statement which is correct about this pointer in c++?",
        "options": [
            "This pointer passed as hidden argument in all non-static variables of the class.",
            "This pointer passed as hidden argument in all static variables of the class.",
            "This pointer passed as hidden argument in all static function of the class.",
            "This pointer passed as hidden argument in all function of the class."
        ],
        "correct_answer": "This pointer passed as hidden argument in all non-static variables of the class.",
        "explanation": "In C++, 'this' pointer is passed to non-static member functions."
    },
    {
        "id": 10,
        "question": "In class diagram, if class Car has solid diamond points to class Engine, what does this indicates?",
        "options": [
            "Car uses Engine temporarily",
            "Engine can exist independently of the Car",
            "Engine is the part of Car and cannot exist without it",
            "Car inherits from Engine"
        ],
        "correct_answer": "Engine is the part of Car and cannot exist without it",
        "explanation": "Solid diamond represents Composition."
    },
    {
        "id": 11,
        "question": "The amount of time the algorithm takes on the smallest possible set of inputs is called_____",
        "options": ["Average time", "Small time", "Worst time", "Best time"],
        "correct_answer": "Best time",
        "explanation": "Minimum execution time is the Best time complexity."
    },
    {
        "id": 12,
        "question": "For a weak entity set to be meaningful, it must be associated with another entity set, called the",
        "options": ["Identifying set", "Strong entity set", "Neighbor set", "Owner set"],
        "correct_answer": "Strong entity set",
        "explanation": "A weak entity set must be linked to a strong entity set."
    },
    {
        "id": 13,
        "question": "Which one of the following is not the application level service?",
        "options": ["Proxies and agents", "Installing a new service", "E-mail configuration", "Quality of service"],
        "correct_answer": "Installing a new service",
        "explanation": "Installing a service is an operational administration task."
    },
    {
        "id": 14,
        "question": "A language that allows the DBA or user to describe and name the entities, attributes, and relationships required for the application is__________",
        "options": ["Transaction control language (TCL)", "Data control language (DCL)", "Data Manipulation Language (DML)", "Data Definition Language (DDL)"],
        "correct_answer": "Data Definition Language (DDL)",
        "explanation": "DDL is used to define database structures."
    },
    {
        "id": 15,
        "question": "Which one of the following is linear data structure?",
        "options": ["Tree", "Array", "Queue", "Linked list"],
        "correct_answer": "Array",
        "explanation": "Array stores elements in sequential linear order."
    },
    {
        "id": 16,
        "question": "What is the main purpose of syntax-directed translation in a compiler?",
        "options": [
            "To interleave semantic analysis with syntax analysis using attributes attached to grammar symbols",
            "To generate optimized machine code directly",
            "To tokenize the source code",
            "To replace the parser with a finite automaton"
        ],
        "correct_answer": "To interleave semantic analysis with syntax analysis using attributes attached to grammar symbols",
        "explanation": "Syntax-directed translation attaches semantic rules to grammar symbols."
    },
    {
        "id": 17,
        "question": "What will be the output of the following program segment?\npublic class Calculation {\n  public static void main(String[] args) {\n    int sum = 0;\n    for(int j = 1; j<=10; j++) {\n      sum = sum + j;\n    }\n    System.out.println(+sum);\n  }\n}",
        "options": ["55", "44", "33", "66"],
        "correct_answer": "55",
        "explanation": "Sum of numbers 1 to 10 is 55."
    },
    {
        "id": 18,
        "question": "Which keyword is used in Java to create a subclass that inherits from a superclass?",
        "options": ["Inherits", "Superclass", "Extends", "Implements"],
        "correct_answer": "Extends",
        "explanation": "Java uses 'extends' for inheritance."
    },
    {
        "id": 19,
        "question": "What is the output of the following C++ code fragment?\nInt a=6, b=8;\nInt x=2, y=4;\nInt c(x>y? (a--; x): (b--; y));\nCout<<\"a\"<<a;\nCout<<\" b=\"<<b;\nCout <<\" c=\"<<c;",
        "options": ["a=6 b=5 c=4", "a=6 b=7 c=5", "a=8 b=6 c=5", "a=6 b=7 c=4"],
        "correct_answer": "a=6 b=7 c=4",
        "explanation": "x>y is false, so it executes (b--; y). b becomes 7, c gets y's value (4)."
    },
    {
        "id": 20,
        "question": "___________is a collection of related fields that can be treated as a unit by some application program.",
        "options": ["Rows", "Field", "Record", "Database"],
        "correct_answer": "Record",
        "explanation": "A record is a collection of related fields."
    },
    {
        "id": 21,
        "question": "Straight directed translation uses:",
        "options": ["Purely lexical rules", "Backtracking algorithms", "Grammar without attributes", "Grammar with sematic rule"],
        "correct_answer": "Grammar with sematic rule",
        "explanation": "Syntax-directed translation relies on grammars with semantic rules."
    },
    {
        "id": 22,
        "question": "Which one of the following is the first operation or step in CPU instruction cycle?",
        "options": ["Executing the instruction", "Handling interrupt", "Decoding the instruction", "Fetching the instruction"],
        "correct_answer": "Fetching the instruction",
        "explanation": "The instruction cycle always starts with Fetching."
    },
    {
        "id": 23,
        "question": "Which search strategy tries to expand the node that is closest to the goal, on the grounds that this is likely to lead to a solution quickly; Thus, it evaluates nodes by using just the heuristic function: f ( n) = h ( n).",
        "options": ["Uniform-cost search", "Greedy best-first search", "Depth-first search", "A* search"],
        "correct_answer": "Greedy best-first search",
        "explanation": "Greedy best-first search evaluates nodes strictly using f(n) = h(n)."
    },
    {
        "id": 24,
        "question": "Which one of the following is a top-down parser without backtracking?",
        "options": ["LR parser", "Brute force parser", "Operator precedence parser", "Predictive parser"],
        "correct_answer": "Predictive parser",
        "explanation": "Predictive parser is a top-down parser without backtracking."
    },
    {
        "id": 25,
        "question": "How many layers are there in OSI reference model?",
        "options": ["7", "6", "5", "4"],
        "correct_answer": "7",
        "explanation": "The OSI model consists of 7 layers."
    },
    {
        "id": 26,
        "question": "Which one of the following is a computer structural component that provides for communication among CPU, main memory and I/O?",
        "options": ["System unit", "Computer network", "CPU", "System interconnection"],
        "correct_answer": "System interconnection",
        "explanation": "System interconnection (buses) bridges CPU, memory, and I/O."
    },
    {
        "id": 27,
        "question": "Assume that we are able to specify that Mr. Getahun can view the database record, but cannot change the value of the record. Which security management technique was used in this scenario?",
        "options": ["Access Control", "Availability", "Non-repudiation", "Integrity"],
        "correct_answer": "Access Control",
        "explanation": "Access Control restricts operations based on user permissions."
    },
    {
        "id": 28,
        "question": "Suppose, a developer proposes using deferred update with no checkpoints in a high-transaction OLTP system. What is the most serious drawback?",
        "options": [
            "Log scans become prohibitively expensive after long uptime",
            "Increased disk I/O due to frequent page copying",
            "Shared locks cannot be used",
            "View serializability cannot be ensured"
        ],
        "correct_answer": "Log scans become prohibitively expensive after long uptime",
        "explanation": "Without checkpoints, log scans during recovery take too long."
    },
    {
        "id": 29,
        "question": "Which one of the following function of operating system is categorized under process management?",
        "options": [
            "Allocates the device in the efficient way",
            "De-allocates the resources.",
            "Allocates the memory when the process requests it to do so.",
            "Allocates the processor (CPU) to a process"
        ],
        "correct_answer": "Allocates the processor (CPU) to a process",
        "explanation": "Process management allocates CPU time to active processes."
    },
    {
        "id": 30,
        "question": "Which of the following statements is TRUE?",
        "options": [
            "Every regular language is context-free.",
            "Every context-free language is regular.",
            "Every context-sensitive language is regular.",
            "Every recursively enumerable language is recursive"
        ],
        "correct_answer": "Every regular language is context-free.",
        "explanation": "According to the Chomsky hierarchy, all Regular languages are Context-Free."
    },
    {
        "id": 31,
        "question": "____________ is a data transfer method in computer organization and architecture that allows an I/O device to transfer data directly to or from memory without the involvement of the CPU.",
        "options": ["Asynchronous data transfer", "Direct Memory Access (DMA)", "Interrupt-driven transfer", "Programmed I/O transfer"],
        "correct_answer": "Direct Memory Access (DMA)",
        "explanation": "DMA allows I/O devices to bypass the CPU for memory transfer."
    },
    {
        "id": 32,
        "question": "Which one of the following php method is used to retrieve the information from the form control through the parameters sent in the URL?",
        "options": ["$_REQUEST[]", "$_POST[]", "$_GET[]", "isset()"],
        "correct_answer": "$_GET[]",
        "explanation": "$_GET retrieves form parameters sent in the URL string."
    },
    {
        "id": 33,
        "question": "Which statement is NOT true about digital signature?",
        "options": [
            "Digital signature is not encryption algorithm",
            "In digital signature Sender encrypts message with its private key",
            "In digital signature Sender encrypts message with its public key",
            "Digital signature provides authentication services"
        ],
        "correct_answer": "In digital signature Sender encrypts message with its public key",
        "explanation": "Digital signatures encrypt hashes using the sender's PRIVATE key, not public key."
    },
    {
        "id": 34,
        "question": "Which one of the following ip address class uses first two octets for network addresses and last two for host addressing?",
        "options": ["Class C", "Class D", "Class A", "Class B"],
        "correct_answer": "Class B",
        "explanation": "Class B IP addresses use 16 bits (2 octets) for network and 16 bits for host."
    },
    {
        "id": 35,
        "question": "Which of the following best defines a heuristic in the context of AI search?",
        "options": [
            "A function that estimates how close a state is to the goal",
            "A guaranteed optimal path to the goal",
            "A method that always avoids revisiting states",
            "A brute-force enumeration of all possible states"
        ],
        "correct_answer": "A function that estimates how close a state is to the goal",
        "explanation": "Heuristic functions estimate remaining path cost to the goal."
    },
    {
        "id": 36,
        "question": "Which one of the following party performs the technical evaluation work, using the evidence supplied by the developers, and additional testing of the product, to confirm that it satisfies the functional and assurance requirements specified in the security target?",
        "options": ["Evaluator", "Certifier", "Sponsor", "Developer"],
        "correct_answer": "Evaluator",
        "explanation": "The Evaluator conducts functional and security testing."
    },
    {
        "id": 37,
        "question": "Assume that you have a huge company like university; bank industry, etc. have their own data center to store and control the different type of the data. Which type of RAID technology is the most preferable to use?",
        "options": ["RAID level 3", "RAID level 1", "RAID level 2", "RAID level 0"],
        "correct_answer": "RAID level 1",
        "explanation": "RAID 1 provides mirroring and high data redundancy suitable for critical data centers."
    },
    {
        "id": 38,
        "question": "Which analysis technique is INAPPROPRIATE for determining the lower bound of comparison-based sorting, and why?",
        "options": [
            "Decision tree model — because it assumes only array indexing is allowed",
            "Recurrence relations — because sorting isn’t naturally recursive",
            "Asymptotic analysis — because it ignores constants",
            "Decision tree model — because it gives an information-theoretic lower bound of Ω(n log n)"
        ],
        "correct_answer": "Recurrence relations — because sorting isn’t naturally recursive",
        "explanation": "Recurrence relations evaluate specific recursive algorithms, not lower bounds of problem classes."
    },
    {
        "id": 39,
        "question": "In CSS, which property is used to change the text color of an element?",
        "options": ["text-color", "font-color", "color", "Foreground"],
        "correct_answer": "color",
        "explanation": "CSS uses 'color' to change text color."
    },
    {
        "id": 40,
        "question": "From the flowing function which one is used to create the table",
        "options": [
            "CREATE table_name (column_name, column type);",
            "CREATE table_name (column_type, column name);",
            "CREATE TABLE table_name (column_name, column type);",
            "CREATE TABLE table_name (column_type, column name);"
        ],
        "correct_answer": "CREATE TABLE table_name (column_name, column type);",
        "explanation": "SQL syntax: CREATE TABLE table_name (column_name data_type)."
    },
    {
        "id": 41,
        "question": "What is the primary function of an operating system?",
        "options": [
            "To connect to the internet",
            "To create documents and spreadsheets",
            "To design computer hardware",
            "To act as an intermediary between users and computer hardware"
        ],
        "correct_answer": "To act as an intermediary between users and computer hardware",
        "explanation": "An OS interfaces between human users and underlying physical hardware."
    },
    {
        "id": 42,
        "question": "How much time units or T( n) taken to compute the following piece of code?\nint total(int n)\n{\n  int sum=0;\n  for (int i=1;i<=n;i++)\n    sum=sum+1;\n  return sum;\n}",
        "options": ["5n+5", "4n2+4", "6n+2", "4n+4"],
        "correct_answer": "6n+2",
        "explanation": "Statement analysis for operation execution counts yields T(n) = 6n+2."
    },
    {
        "id": 43,
        "question": "An object oriented principle that contains information in an object, exposing only selected information is____________.",
        "options": ["Abstraction", "Inheritance", "Polymorphism", "Encapsulation"],
        "correct_answer": "Encapsulation",
        "explanation": "Encapsulation wraps data and restricts direct outside access."
    },
    {
        "id": 44,
        "question": "Stack is follows ____policy:",
        "options": ["LIFO", "FIFO", "FILO", "FCFS"],
        "correct_answer": "LIFO",
        "explanation": "Stack uses Last-In, First-Out (LIFO)."
    },
    {
        "id": 45,
        "question": "From the following alternatives which one is FALSE about database system?",
        "options": [
            "It is very difficult to protect a file under the system",
            "In database system the user is not required to write the procedures",
            "In database system, DBMS provides a good protection mechanism.",
            "It contains a wide variety of sophisticated techniques to store and retrieve the data."
        ],
        "correct_answer": "It is very difficult to protect a file under the system",
        "explanation": "DBMS provides robust built-in data security features."
    },
    {
        "id": 46,
        "question": "Which one of the following is categorized under Log based Recovery Techniques in database?",
        "options": ["Recovery in Multi-database Systems", "ARIES Recovery Algorithm", "Shadow Paging Technique", "Deferred Database Modification"],
        "correct_answer": "ARIES Recovery Algorithm",
        "explanation": "ARIES is a standard log-based transaction recovery algorithm."
    },
    {
        "id": 47,
        "question": "What is the first step to convert context free grammar (CFG) into Greibach Normal Form (GNF)?",
        "options": [
            "Convert the grammar into CNF",
            "If any production rule in the grammar is not in GNF form, convert it.",
            "Convert the grammar into GNF",
            "If the grammar exists left recursion, eliminate it."
        ],
        "correct_answer": "If the grammar exists left recursion, eliminate it.",
        "explanation": "Left recursion must be eliminated prior to GNF conversion."
    },
    {
        "id": 48,
        "question": "A user installs a new printer. The OS automatically detects and configures it. This is an example of:",
        "options": ["Plug-and-play functionality", "Manual driver installation", "Manual hardware management", "Resource allocation"],
        "correct_answer": "Plug-and-play functionality",
        "explanation": "Automatic hardware configuration is called Plug-and-play."
    },
    {
        "id": 49,
        "question": "Which of the following is NOT property of an algorithm?",
        "options": ["Finiteness", "Definiteness", "Correctness", "Platform dependence"],
        "correct_answer": "Platform dependence",
        "explanation": "Algorithms must be platform-independent logical procedures."
    },
    {
        "id": 50,
        "question": "Which Redundant Array of Independent Disks (RAID) is known by striping with parity and fault tolerance?",
        "options": ["RAID 2", "RAID 1", "RAID 5", "RAID 0"],
        "correct_answer": "RAID 5",
        "explanation": "RAID 5 provides block-level striping with distributed parity."
    },
    {
        "id": 51,
        "question": "Assume that you are computer science expert and you need to develop large programs within short period of time. Finally, you have planned to provide portable program to the concerned body. Which type of programming language is preferable for the above scenario?",
        "options": ["Low level", "Machine level", "High level", "Assembly"],
        "correct_answer": "High level",
        "explanation": "High-level languages provide portability and fast development speed."
    },
    {
        "id": 52,
        "question": "Which type of heuristic search strategy that evaluates nodes by combining g ( n), the cost to reach the node, and h ( n.), the cost to get from the node to the goal: f ( n) = g ( n) + h ( n)?",
        "options": ["A* search", "Greedy Best-First Search", "Uniform-cost search", "Depth-first search"],
        "correct_answer": "A* search",
        "explanation": "A* search evaluates using f(n) = g(n) + h(n)."
    },
    {
        "id": 53,
        "question": "If input is “a” is for syntax tree, which function is used to create tree?",
        "options": ["mknode(num, value)", "mkleaf(num, value)", "mkleaf(id, entry)", "mknode(op, left, right)"],
        "correct_answer": "mknode(op, left, right)",
        "explanation": "mknode constructs interior tree nodes with operators and children pointers."
    },
    {
        "id": 54,
        "question": "Suppose Mr. Negesa might act as Mr. Dereje and send message to Registrar X, the registrar might be lead to believe that message indeed come from Mr. Dereje. What types of attack Mr. Negesa has committed?",
        "options": ["Denial of service", "Modification of message", "Masquerade", "Replay"],
        "correct_answer": "Masquerade",
        "explanation": "Impersonating another identity is a Masquerade attack."
    },
    {
        "id": 55,
        "question": "From the following statement which one is disadvantage of waterfall model?",
        "options": [
            "model is simple and easy to understand and use",
            "It is easy manage due to the rigidity of the model",
            "Not suitable for projects where requirements are at a moderate to high risk of changing",
            "In this model phases are processed and completed one at a time"
        ],
        "correct_answer": "Not suitable for projects where requirements are at a moderate to high risk of changing",
        "explanation": "Waterfall model handles changing requirement poorly due to sequential design."
    },
    {
        "id": 56,
        "question": "Consider a directed line(->) from the relationship set advisor to both entity sets instructor and student. This indicates _________ cardinality",
        "options": ["Many to one", "Many to many", "One to one", "One to many"],
        "correct_answer": "Many to one",
        "explanation": "Arrows directed to entity sets indicate 'One' side bounds."
    },
    {
        "id": 57,
        "question": "In a system, resources cannot be forcibly taken from processes; they must be released voluntarily. Which deadlock condition does this represent?",
        "options": ["No Preemption", "Hold and Wait", "Mutual Exclusion", "Circular Wait"],
        "correct_answer": "No Preemption",
        "explanation": "No Preemption means resources cannot be forcibly confiscated."
    },
    {
        "id": 58,
        "question": "Which statement is WRONGLY described about code generation?",
        "options": [
            "Code generation can be considered as the start phase of compilation",
            "The target program is the output of the code generator",
            "The code generation phase needs complete error-free intermediate code as an input requires",
            "It used to produce the target code for three-address statements."
        ],
        "correct_answer": "Code generation can be considered as the start phase of compilation",
        "explanation": "Code generation is the FINAL phase of compilation, not the start."
    },
    {
        "id": 59,
        "question": "____________is a service that allows organizations and individuals to post a website or a web page onto the Internet.",
        "options": ["Web hosting", "Internet service provider", "Web client", "Domain name registration"],
        "correct_answer": "Web hosting",
        "explanation": "Web hosting provides server space for public web pages."
    },
    {
        "id": 60,
        "question": "In singly linked list, the node contains",
        "options": ["Data and index", "Data and one pointer ( the next node)", "Only data", "Data and two pointers"],
        "correct_answer": "Data and one pointer ( the next node)",
        "explanation": "Singly linked list nodes store data and a next node pointer."
    },
    {
        "id": 61,
        "question": "Which of the following statement is non-functional requirement?",
        "options": [
            "The system allow user to generate PDF report.",
            "The system respond to user’s request within 2 second under normal load",
            "The system allow user to store data on relational database",
            "The system allow user to submit emergency report"
        ],
        "correct_answer": "The system respond to user’s request within 2 second under normal load",
        "explanation": "Performance criteria are non-functional requirements."
    },
    {
        "id": 62,
        "question": "In object design, what does the contract typically includes?",
        "options": ["The class diagram and sequence diagram", "Project budget and timeline", "Invariants, preconditions, post conditions", "The use case names and actors role"],
        "correct_answer": "Invariants, preconditions, post conditions",
        "explanation": "Design by contract uses preconditions, postconditions, and invariants."
    },
    {
        "id": 63,
        "question": "Which of the following OSI layers is NOT correctly matched to its corresponding data Units (PDU)?",
        "options": ["Application layer ---> Data", "Transport layer ---> Segment", "Physical layer ---> Bit", "Network layer ---> Frame"],
        "correct_answer": "Network layer ---> Frame",
        "explanation": "Network layer PDU is Packet; Data Link layer PDU is Frame."
    },
    {
        "id": 64,
        "question": "Which data structure follows LIFO principle?",
        "options": ["Graphs", "Queues", "Stacks", "Trees"],
        "correct_answer": "Stacks",
        "explanation": "Stacks follow Last-In-First-Out."
    },
    {
        "id": 65,
        "question": "Consider the following code snippet\nclass Animal { void sound() { System.out.println(\"Animal sound\"); } }\nclass Dog extends Animal { void sound() { System.out.println(\"Bark!\"); } }\nWhich OOP concept is illustrated when Dog provides its own version of sound?",
        "options": ["Method overriding", "Method overloading", "Abstraction", "Encapsulation"],
        "correct_answer": "Method overriding",
        "explanation": "Redefining a superclass method in a subclass is Method Overriding."
    },
    {
        "id": 66,
        "question": "Which type of grammar is used to generate all possible patterns of strings in a given formal language?",
        "options": ["Context-free", "Context-sensitive", "Recursively enumerable", "Regular"],
        "correct_answer": "Recursively enumerable",
        "explanation": "Recursively enumerable grammars generate arbitrary formal languages."
    },
    {
        "id": 67,
        "question": "Which tool is used to troubleshoot the network connectivity?",
        "options": ["Ipconfig", "Ping", "Encryption", "Firewall"],
        "correct_answer": "Ping",
        "explanation": "Ping checks end-to-end IP reachability."
    },
    {
        "id": 68,
        "question": "The time complexity for binary search is__________",
        "options": ["O(n*log(n )2)", "O(n2)", "O( n)", "O(logn)"],
        "correct_answer": "O(logn)",
        "explanation": "Binary search has logarithmic runtime O(log n)."
    },
    {
        "id": 69,
        "question": "Which type of access specifier is accessible within the same package or subclasses in a different package?",
        "options": ["Public", "Default", "Private", "Protected"],
        "correct_answer": "Protected",
        "explanation": "Protected scope includes package members and derived subclasses."
    },
    {
        "id": 70,
        "question": "What is the basic goal of Normalization?",
        "options": ["To decrease data integrity", "To reduce redundancy", "To maximize transitive dependency", "To increase dependency"],
        "correct_answer": "To reduce redundancy",
        "explanation": "Normalization minimizes duplicate data storage."
    },
    {
        "id": 71,
        "question": "Which protocol is mostly used for communication between client and server in a web application?",
        "options": ["FTP", "SMTP", "HTTP", "SSH"],
        "correct_answer": "HTTP",
        "explanation": "HTTP/HTTPS is the primary web application communications protocol."
    },
    {
        "id": 72,
        "question": "Which of the following layers is responsible for encryption, translation and compression?",
        "options": ["Presentation layer", "Data link layer", "Transport layer", "Network layer"],
        "correct_answer": "Presentation layer",
        "explanation": "Presentation layer manages encoding, formatting, and encryption."
    },
    {
        "id": 73,
        "question": "What is the extension of JavaScript file?",
        "options": [".javaS", ".JS", ".java", "CSS"],
        "correct_answer": ".JS",
        "explanation": "JavaScript files use the .js extension."
    },
    {
        "id": 74,
        "question": "Why is perception still a challenge for AI—even though systems can recognize faces?",
        "options": [
            "Because perception is unrelated to reasoning",
            "Because AI lacks actuators",
            "Because perception requires common-sense knowledge and robust natural language understanding in open ended worlds",
            "Because sensors are too expensive"
        ],
        "correct_answer": "Because perception requires common-sense knowledge and robust natural language understanding in open ended worlds",
        "explanation": "Perception requires contextual reasoning in unstructured environments."
    },
    {
        "id": 75,
        "question": "Which service used to translate domain names to ip address?",
        "options": ["HTTPS", "DHCP", "HTTP", "DNS"],
        "correct_answer": "DNS",
        "explanation": "DNS maps domain names to IP addresses."
    },
    {
        "id": 76,
        "question": "Which one of following monitors incoming and outgoing network traffic and decides whether to allow or block specific traffic based on a defined set of security rules?",
        "options": ["Intrusion detection system (IDS)", "Proxy server", "Virtual Private network", "Firewall"],
        "correct_answer": "Firewall",
        "explanation": "Firewalls filter network traffic against rule sets."
    },
    {
        "id": 77,
        "question": "Consider attributes ID, CITY and NAME. Which one of this can be considered as a super key?",
        "options": ["NAME", "ID", "CITY", "CITY, ID"],
        "correct_answer": "CITY, ID",
        "explanation": "A super key is any set of attributes containing a candidate key (ID)."
    },
    {
        "id": 78,
        "question": "You want to ensure that a method calculateTax() in class Employee cannot be overridden by any subclass. What declaration achieves this?",
        "options": ["Abstract double calculateTax();", "Final double calculateTax(){…}", "Private double calculateTax(){…}", "Static double calculateTax(){…}"],
        "correct_answer": "Final double calculateTax(){…}",
        "explanation": "'final' keyword prevents method overriding."
    },
    {
        "id": 79,
        "question": "Which one of the following identifier name is INVALID in C++ programming language?",
        "options": ["delete", "for_cpp", "jan2025", "Hello"],
        "correct_answer": "delete",
        "explanation": "'delete' is a reserved keyword in C++."
    },
    {
        "id": 80,
        "question": "Which one of the following UML building block that defines the static part of the model and represents physical and conceptual elements?",
        "options": ["Structural things", "Behavioral things", "An notational things", "Grouping things"],
        "correct_answer": "Structural things",
        "explanation": "Structural things represent static elements in UML."
    },
    {
        "import_id": 81,
        "id": 81,
        "question": "Which scenario is best suited for UDP rather than TCP protocol?",
        "options": ["Live video streaming", "Email transmission", "Downloading the files", "Database update"],
        "correct_answer": "Live video streaming",
        "explanation": "UDP fits low-latency streaming applications."
    },
    {
        "id": 82,
        "question": "Which type of transparency in distributed database system distributes a relation into sub relations where each sub relation is defined by a subset of the columns of the original relation?",
        "options": ["Replication", "Location", "Horizontal", "Vertical"],
        "correct_answer": "Vertical",
        "explanation": "Vertical fragmentation splits table columns."
    },
    {
        "id": 83,
        "question": "In which of the following Learning methods an agent receives feedback in the form of rewards or penalties to maximize cumulative reward?",
        "options": ["Supervised learning", "Reinforcement learning", "Semi-supervised learning", "Unsupervised learning"],
        "correct_answer": "Reinforcement learning",
        "explanation": "Reinforcement learning learns from rewards and penalties."
    },
    {
        "id": 84,
        "question": "After deploying a new software system, users reports that the system slows during peak hour. Which software quality attribute primarily affected?",
        "options": ["Maintainability", "Performance", "Reliability", "Usability"],
        "correct_answer": "Performance",
        "explanation": "System speed and response time fall under Performance."
    },
    {
        "id": 85,
        "question": "Which one of the following is WRONGLY stated about an importance of security policy?",
        "options": ["To help minimize risk.", "To ensure the confidentiality, integrity and availability of data.", "To coordinate and enforce a security program across an organization.", "To use the system in a passive way"],
        "correct_answer": "To use the system in a passive way",
        "explanation": "Using systems passively is not a security policy goal."
    },
    {
        "id": 86,
        "question": "Which of the following is NOT a task of the lexical analyzer?",
        "options": ["Generating parse trees", "Correlating errors with line numbers", "Entering identifiers into the symbol table", "Stripping whitespace and comments"],
        "correct_answer": "Generating parse trees",
        "explanation": "Generating parse trees is done by the Parser/Syntax Analyzer."
    },
    {
        "id": 87,
        "question": "Which sorting algorithm compares each pair of adjacent elements from the beginning of an array and, if they are in reversed order, swaps them; if at least one swaps has been done, repeat step 1.",
        "options": ["Insertion sort", "Bubble sort", "Selection sort", "Shell sort"],
        "correct_answer": "Bubble sort",
        "explanation": "Bubble sort works by repeatedly swapping adjacent out-of-order elements."
    },
    {
        "id": 88,
        "question": "Which one of the following computer security goal prevents the disclosure of sensitive information to unauthorized users or systems on computer networks?",
        "options": ["Confidentiality", "Integrity", "Cyberspace", "Availability"],
        "correct_answer": "Confidentiality",
        "explanation": "Confidentiality prevents unauthorized data disclosure."
    },
    {
        "id": 89,
        "question": "Assume that you have IPv4 addresses in binary notation 11000001 10000011 00011011 11111111 and you are requested to change into dotted decimal notation. What is the equivalent IP address in decimal dotted notation?",
        "options": ["192.174.27.255", "192.134.67.254", "193.130.28.254", "193.131.27.255"],
        "correct_answer": "193.131.27.255",
        "explanation": "11000001=193, 10000011=131, 00011011=27, 11111111=255."
    },
    {
        "id": 90,
        "question": "You have given that Grammar G1 −({S, A, B}, {a, b}, S, {S → AB, A → a, B → b}). Which one is terminal symbol in the give?",
        "options": ["a,b", "S", "S → AB, A → a, B → b", "S,A,B"],
        "correct_answer": "a,b",
        "explanation": "Lowercase letters {a, b} represent terminal symbols."
    },
    {
        "id": 91,
        "question": "Among the following one is NOT the application of queue in the real world.",
        "options": [
            "It is used in operating systems for handling interrupts.",
            "It is used to maintain the play list in media players in order",
            "It is used in Depth First search",
            "It is widely used as waiting lists for a single shared resource"
        ],
        "correct_answer": "It is used in Depth First search",
        "explanation": "Depth First Search uses a Stack, not a Queue."
    },
    {
        "id": 92,
        "question": "Which one of the following is disadvantage of circuit switching?",
        "options": ["Predictable performance", "Low latency", "Guaranteed bandwidth", "Limited scalability"],
        "correct_answer": "Limited scalability",
        "explanation": "Circuit switching has limited resource scalability."
    },
    {
        "id": 93,
        "question": "A developer stores user login status in both $_SESSION['user_id'] on the server and document.cookie = \"logged_in=1\" on the client. An attacker tampers with cookies to set logged_in=1 without authenticating. Which statement is the most accurate?",
        "options": [
            "The system is vulnerable — cookie-only checks bypass server session validation",
            "The system is secure — session data cannot be forged without the server-side secret",
            "The system is vulnerable only if session_id is exposed",
            "The system is secure if HTTPS is used,"
        ],
        "correct_answer": "The system is vulnerable — cookie-only checks bypass server session validation",
        "explanation": "Relying on client-controlled cookies for authentication bypasses server security."
    },
    {
        "id": 94,
        "question": "The language L = {wwᴿ | w ∈ {a, b}*} (even-length palindromes) is:",
        "options": ["Regular", "Non-deterministic CFL but not deterministic", "Deterministic CFL", "Context-sensitive but not context-free"],
        "correct_answer": "Non-deterministic CFL but not deterministic",
        "explanation": "Even-length palindromes require a non-deterministic pushdown automaton."
    },
    {
        "id": 95,
        "question": "______________is one of the candidate keys chosen by the database designer to uniquely identify the entity set.",
        "options": ["Super key", "Candidate key", "Social security key", "Primary key"],
        "correct_answer": "Primary key",
        "explanation": "The Primary Key is the chosen candidate key for unique identification."
    },
    {
        "id": 96,
        "question": "Which of the following statement about function overloading is TRUE?",
        "options": [
            "Overload function have same name but different parameters/type",
            "Overload function is not supported",
            "Overload function must have different return type",
            "Overload function must have the same number of parameters"
        ],
        "correct_answer": "Overload function have same name but different parameters/type",
        "explanation": "Overloaded functions share names with distinct parameter signatures."
    },
    {
        "id": 97,
        "question": "How does an operating system improve efficiency in a multi-user environment?",
        "options": [
            "By allowing only one user to access the system at a time",
            "By disabling all background services",
            "By using time-sharing and process scheduling to allocate CPU time fairly among users and processes",
            "By requiring manual intervention for each task"
        ],
        "correct_answer": "By using time-sharing and process scheduling to allocate CPU time fairly among users and processes",
        "explanation": "Time-sharing schedules multi-user CPU processing."
    },
    {
        "id": 98,
        "question": "Which one of the following is not feature of dynamic web page?",
        "options": [
            "Contents can be generated on-the-fly",
            "Changing content or lively",
            "Contain the same prebuilt content each time the page is loaded",
            "Ability to connect to a database"
        ],
        "correct_answer": "Contain the same prebuilt content each time the page is loaded",
        "explanation": "Prebuilt fixed content is a feature of STATIC web pages, not dynamic."
    },
    {
        "id": 99,
        "question": "Why should form <input> elements include an associated <label> with the for attribute?",
        "options": [
            "It enables offline form storage",
            "It encrypts user data",
            "It increases form submission speed",
            "It improves accessibility: screen readers announce the label when the input is focused"
        ],
        "correct_answer": "It improves accessibility: screen readers announce the label when the input is focused",
        "explanation": "Explicit labels improve web accessibility for assistive technologies."
    },
    {
        "id": 100,
        "question": "Question number 100",
        "options": ["A", "B", "C", "D"],
        "correct_answer": "C",
        "explanation": "Answer specified as option C."
    }
]