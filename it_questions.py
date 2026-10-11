# it_questions.py

IT_EXIT_EXAM = [
    {
        'id': 1,
        'question': "Which layer of the OSI model is responsible for routing packets across different networks?",
        'options': [
            'A. Physical Layer',
            'B. Data Link Layer',
            'C. Network Layer',
            'D. Transport Layer',
            'E. Application Layer'
        ],
        'correct_answer': 'C. Network Layer',
        'explanation': "The Network Layer (Layer 3) handles packet routing, forwarding, and logical addressing (IP addressing) across distinct networks."
    },
    {
        'id': 2,
        'question': "What is the primary function of the Address Resolution Protocol (ARP)?",
        'options': [
            'A. To map an IP address to a MAC address',
            'B. To assign IP addresses dynamically to hosts',
            'C. To translate domain names into IP addresses',
            'D. To secure data transmitted across a local network',
            'E. None of the above'
        ],
        'correct_answer': 'A. To map an IP address to a MAC address',
        'explanation': "ARP resolves a known IPv4 address into its corresponding physical hardware MAC address on a local area network."
    },
    {
        'id': 3,
        'question': "Which of the following SQL statements is used to retrieve unique values from a table column?",
        'options': [
            'A. SELECT UNIQUE',
            'B. SELECT DISTINCT',
            'C. SELECT DIFFERENT',
            'D. SELECT SINGLE',
            'E. SELECT UNIQUE-ROW'
        ],
        'correct_answer': 'B. SELECT DISTINCT',
        'explanation': "The DISTINCT keyword in SQL is used to eliminate duplicate rows and return only unique values from the specified columns."
    },
    {
        'id': 4,
        'question': "In Object-Oriented Programming (OOP), what principle allows a subclass to provide a specific implementation of a method already defined in its superclass?",
        'options': [
            'A. Encapsulation',
            'B. Method Overloading',
            'C. Method Overriding',
            'D. Abstraction',
            'E. Inheritance'
        ],
        'correct_answer': 'C. Method Overriding',
        'explanation': "Method overriding allows a sub-class or child class to provide a specific implementation of a method that is already provided by its parent class."
    },
    {
        'id': 5,
        'question': "Which protocol is used by web browsers to securely transmit web pages over the Internet?",
        'options': [
            'A. HTTP',
            'B. FTP',
            'C. HTTPS',
            'D. SMTP',
            'E. Telnet'
        ],
        'correct_answer': 'C. HTTPS',
        'explanation': "HTTPS (Hypertext Transfer Protocol Secure) encrypts web traffic using SSL/TLS for secure communication over the web."
    },
    {
        'id': 6,
        'question': "What is the default port number used by HTTP?",
        'options': [
            'A. 21',
            'B. 80',
            'C. 443',
            'D. 8080',
            'E. 25'
        ],
        'correct_answer': 'B. 80',
        'explanation': "Standard unencrypted HTTP web traffic defaults to TCP port 80."
    },
    {
        'id': 7,
        'question': "In relational database design, a key that uniquely identifies each record in a table is called a:",
        'options': [
            'A. Foreign Key',
            'B. Composite Key',
            'C. Primary Key',
            'D. Candidate Key',
            'E. Secondary Key'
        ],
        'correct_answer': 'C. Primary Key',
        'explanation': "A Primary Key uniquely identifies each individual record/row inside a database table without allowing nulls."
    },
    {
        'id': 8,
        'question': "Which CPU scheduling algorithm executes the process with the smallest remaining execution time first?",
        'options': [
            'A. First-Come, First-Served (FCFS)',
            'B. Shortest Remaining Time First (SRTF)',
            'C. Round Robin (RR)',
            'D. Priority Scheduling',
            'E. Multilevel Queue'
        ],
        'correct_answer': 'B. Shortest Remaining Time First (SRTF)',
        'explanation': "SRTF is the preemptive version of Shortest Job First, where the process with the smallest time remaining is scheduled next."
    },
    {
        'id': 9,
        'question': "What type of software testing focuses on examining the internal structure, code, and design of the application?",
        'options': [
            'A. Black-Box Testing',
            'B. White-Box Testing',
            'C. Acceptance Testing',
            'D. Usability Testing',
            'E. Alpha Testing'
        ],
        'correct_answer': 'B. White-Box Testing',
        'explanation': "White-box testing tests internal logic, paths, structure, and implementation details of software source code."
    },
    {
        'id': 10,
        'question': "Which data structure operates on a Last-In, First-Out (LIFO) basis?",
        'options': [
            'A. Queue',
            'B. Stack',
            'C. Linked List',
            'D. Tree',
            'E. Graph'
        ],
        'correct_answer': 'B. Stack',
        'explanation': "A Stack follows the Last-In, First-Out (LIFO) principle, where elements are added and removed from the same end (top)."
    },
    {
        'id': 11,
        'question': "What is the main purpose of Network Address Translation (NAT)?",
        'options': [
            'A. To encrypt data sent over the Internet',
            'B. To map private IP addresses to a public IP address',
            'C. To automatically configure DNS settings',
            'D. To prevent Denial of Service (DoS) attacks',
            'E. To assign MAC addresses to network interfaces'
        ],
        'correct_answer': 'B. To map private IP addresses to a public IP address',
        'explanation': "NAT allows multiple devices on a private local network to share a single public IP address when communicating externally."
    },
    {
        'id': 12,
        'question': "In Software Engineering, which process model follows a linear, sequential approach through distinct phases?",
        'options': [
            'A. Agile Model',
            'B. Waterfall Model',
            'C. Spiral Model',
            'D. Scrum Model',
            'E. Prototyping Model'
        ],
        'correct_answer': 'B. Waterfall Model',
        'explanation': "The Waterfall model is a linear sequential life cycle model where progress flows downwards through discrete phases."
    },
    {
        'id': 13,
        'question': "Which command in Linux is used to change file permissions?",
        'options': [
            'A. chown',
            'B. chmod',
            'C. chgrp',
            'D. sudo',
            'E. umask'
        ],
        'correct_answer': 'B. chmod',
        'explanation': "The 'chmod' (change mode) command modifies file or directory access permissions in Unix/Linux systems."
    },
    {
        'id': 14,
        'question': "What does the term 'Normalization' mean in Database Management Systems (DBMS)?",
        'options': [
            'A. The process of encrypting sensitive database records',
            'B. Organizing data to minimize redundancy and dependency',
            'C. Converting a relational database into a NoSQL database',
            'D. Creating backup copies of primary database tables',
            'E. Indexing all columns for faster searches'
        ],
        'correct_answer': 'B. Organizing data to minimize redundancy and dependency',
        'explanation': "Normalization structures relational database tables to reduce data redundancy and improve data integrity."
    },
    {
        'id': 15,
        'question': "Which malicious software masquerades as legitimate software to trick users into installing it?",
        'options': [
            'A. Worm',
            'B. Virus',
            'C. Trojan Horse',
            'D. Spyware',
            'E. Adware'
        ],
        'correct_answer': 'C. Trojan Horse',
        'explanation': "A Trojan horse appears useful or safe but contains hidden malicious code designed to compromise systems."
    },
    {
        'id': 16,
        'question': "Which network topology connects all devices to a single central network device like a switch or hub?",
        'options': [
            'A. Bus Topology',
            'B. Ring Topology',
            'C. Star Topology',
            'D. Mesh Topology',
            'E. Tree Topology'
        ],
        'correct_answer': 'C. Star Topology',
        'explanation': "In a star topology, each node is independently connected to a central hub, switch, or computer."
    },
    {
        'id': 17,
        'question': "What is the time complexity of searching for an element in a balanced Binary Search Tree (BST)?",
        'options': [
            'A. O(1)',
            'B. O(n)',
            'C. O(log n)',
            'D. O(n log n)',
            'E. O(n²)'
        ],
        'correct_answer': 'C. O(log n)',
        'explanation': "In a balanced BST, search operations halve the search space at each step, resulting in logarithmic time complexity O(log n)."
    },
    {
        'id': 18,
        'question': "In web development, which language is primarily used to define the layout and style of a web page?",
        'options': [
            'A. HTML',
            'B. CSS',
            'C. JavaScript',
            'D. PHP',
            'E. Python'
        ],
        'correct_answer': 'B. CSS',
        'explanation': "Cascading Style Sheets (CSS) determines visual styling, colors, fonts, and layout structures for HTML elements."
    },
    {
        'id': 19,
        'question': "Which port number is used by the Secure Shell (SSH) protocol?",
        'options': [
            'A. 20',
            'B. 22',
            'C. 23',
            'D. 25',
            'E. 53'
        ],
        'correct_answer': 'B. 22',
        'explanation': "Secure Shell (SSH) connections securely operate on TCP port 22 by default."
    },
    {
        'id': 20,
        'question': "What condition must occur for a Deadlock to exist in an Operating System?",
        'options': [
            'A. Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait',
            'B. Preemption, Sharing, Round-Robin, Paging',
            'C. Semaphore, Mutex, Deadlock Prevention, Paging',
            'D. Priority Inversion, Multithreading, Memory Leak, Starvation',
            'E. Thrashing, Virtual Memory, Context Switching, Interrups'
        ],
        'correct_answer': 'A. Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait',
        'explanation': "Coffman conditions specify that deadlock requires Mutual Exclusion, Hold & Wait, No Preemption, and Circular Wait simultaneously."
    },
    {
        'id': 21,
        'question': "Which Cloud Computing service model provides hardware, virtualized servers, and networking infrastructure to users?",
        'options': [
            'A. Software as a Service (SaaS)',
            'B. Platform as a Service (PaaS)',
            'C. Infrastructure as a Service (IaaS)',
            'D. Function as a Service (FaaS)',
            'E. Data as a Service (DaaS)'
        ],
        'correct_answer': 'C. Infrastructure as a Service (IaaS)',
        'explanation': "IaaS offers foundational compute resources like virtual machines, storage, and networking over the cloud."
    },
    {
        'id': 22,
        'question': "In IPv4 addressing, how many bits long is an IP address?",
        'options': [
            'A. 16 bits',
            'B. 32 bits',
            'C. 64 bits',
            'D. 128 bits',
            'E. 256 bits'
        ],
        'correct_answer': 'B. 32 bits',
        'explanation': "An IPv4 address consists of 32 bits, typically represented as four octets in dotted-decimal notation."
    },
    {
        'id': 23,
        'question': "How many bits are in an IPv6 address?",
        'options': [
            'A. 32 bits',
            'B. 64 bits',
            'C. 128 bits',
            'D. 256 bits',
            'E. 512 bits'
        ],
        'correct_answer': 'C. 128 bits',
        'explanation': "IPv6 addresses use 128 bits to vastly expand the available address space compared to IPv4."
    },
    {
        'id': 24,
        'question': "Which DBMS integrity constraint ensures that foreign key values in a child table match primary key values in a parent table?",
        'options': [
            'A. Entity Integrity',
            'B. Referential Integrity',
            'C. Domain Integrity',
            'D. User-Defined Integrity',
            'E. Column Integrity'
        ],
        'correct_answer': 'B. Referential Integrity',
        'explanation': "Referential integrity maintains consistency between related tables so foreign keys always point to valid parent records."
    },
    {
        'id': 25,
        'question': "Which cryptography method uses the same key for both encryption and decryption?",
        'options': [
            'A. Asymmetric Encryption',
            'B. Symmetric Encryption',
            'C. Public Key Cryptography',
            'D. Hashing',
            'E. Digital Signatures'
        ],
        'correct_answer': 'B. Symmetric Encryption',
        'explanation': "Symmetric encryption relies on a single shared secret key for both encrypting plaintext and decrypting ciphertext."
    },
    {
        'id': 26,
        'question': "What does HTML stand for?",
        'options': [
            'A. Hyper Text Markup Language',
            'B. High Text Machine Language',
            'C. Hyperlinks and Text Markup Language',
            'D. Home Tool Markup Language',
            'E. Hyper Transfer Model Language'
        ],
        'correct_answer': 'A. Hyper Text Markup Language',
        'explanation': "HTML is the standard markup language used for structuring web pages and applications."
    },
    {
        'id': 27,
        'question': "Which HTTP response status code represents 'Not Found'?",
        'options': [
            'A. 200',
            'B. 301',
            'C. 404',
            'D. 500',
            'E. 403'
        ],
        'correct_answer': 'C. 404',
        'explanation': "Status code 404 indicates that the server cannot find the requested resource or URL."
    },
    {
        'id': 28,
        'question': "What is the primary role of a DNS (Domain Name System) server?",
        'options': [
            'A. To block unauthorized incoming network traffic',
            'B. To translate domain names (e.g., example.com) to IP addresses',
            'C. To assign dynamic IP addresses to connected workstations',
            'D. To host database files for web applications',
            'E. To route packets across autonomous systems'
        ],
        'correct_answer': 'B. To translate domain names (e.g., example.com) to IP addresses',
        'explanation': "DNS acts as the phonebook of the internet, translating human-readable domain names into numerical IP addresses."
    },
    {
        'id': 29,
        'question': "Which of the following is an example of an Agile Software Development framework?",
        'options': [
            'A. Waterfall',
            'B. Scrum',
            'C. V-Model',
            'D. Big Bang Model',
            'E. Incremental Model'
        ],
        'correct_answer': 'B. Scrum',
        'explanation': "Scrum is a popular iterative and incremental agile framework for managing complex product development."
    },
    {
        'id': 30,
        'question': "Which data structure operates on a First-In, First-Out (FIFO) basis?",
        'options': [
            'A. Stack',
            'B. Queue',
            'C. Array',
            'D. Tree',
            'E. Heap'
        ],
        'correct_answer': 'B. Queue',
        'explanation': "A Queue operates on FIFO, where elements are inserted at the back and removed from the front."
    },
    {
        'id': 31,
        'question': "What is the purpose of the SQL GROUP BY clause?",
        'options': [
            'A. To sort query results in ascending order',
            'B. To filter individual rows based on a specific condition',
            'C. To group rows that have the same values into summary rows',
            'D. To join two or more tables together',
            'E. To restrict duplicate rows'
        ],
        'correct_answer': 'C. To group rows that have the same values into summary rows',
        'explanation': "GROUP BY aggregates identical data rows together to calculate summary values using functions like COUNT, SUM, or AVG."
    },
    {
        'id': 32,
        'question': "Which device operates at the Data Link Layer (Layer 2) of the OSI model?",
        'options': [
            'A. Router',
            'B. Hub',
            'C. Switch',
            'D. Repeater',
            'E. Gateway'
        ],
        'correct_answer': 'C. Switch',
        'explanation': "Network switches operate at Layer 2, forwarding frames based on physical MAC addresses."
    },
    {
        'id': 33,
        'question': "What type of attack involves overwhelming a server with flooding traffic to make it unavailable?",
        'options': [
            'A. SQL Injection',
            'B. Cross-Site Scripting (XSS)',
            'C. Distributed Denial of Service (DDoS)',
            'D. Man-in-the-Middle (MitM)',
            'E. Phishing'
        ],
        'correct_answer': 'C. Distributed Denial of Service (DDoS)',
        'explanation': "A DDoS attack floods target servers or networks with massive traffic from multiple sources to exhaust resources."
    },
    {
        'id': 34,
        'question': "In Java, which keyword is used to prevent a class from being inherited?",
        'options': [
            'A. static',
            'B. abstract',
            'C. final',
            'D. private',
            'E. protected'
        ],
        'correct_answer': 'C. final',
        'explanation': "Declaring a Java class as 'final' stops other classes from extending or subclassing it."
    },
    {
        'id': 35,
        'question': "Which operating system mechanism divides physical memory into fixed-size blocks called frames and logical memory into pages?",
        'options': [
            'A. Segmentation',
            'B. Paging',
            'C. Virtualization',
            'D. Swapping',
            'E. Compaction'
        ],
        'correct_answer': 'B. Paging',
        'explanation': "Paging maps fixed-size logical memory pages into equal-sized physical memory frames to manage RAM efficiently."
    },
    {
        'id': 36,
        'question': "What is the primary advantage of Using RAID 1 in a storage server?",
        'options': [
            'A. Data Mirroring (Fault Tolerance)',
            'B. Data Striping without Parity',
            'C. Maximum Storage Efficiency',
            'D. High-speed Compression',
            'E. Distributed Parity'
        ],
        'correct_answer': 'A. Data Mirroring (Fault Tolerance)',
        'explanation': "RAID 1 duplicates identical data across multiple drives (mirroring), providing redundancy if one drive fails."
    },
    {
        'id': 37,
        'question': "Which Git command creates a local copy of a remote repository?",
        'options': [
            'A. git pull',
            'B. git clone',
            'C. git commit',
            'D. git push',
            'E. git init'
        ],
        'correct_answer': 'B. git clone',
        'explanation': "'git clone' downloads an existing remote repository onto your local machine along with its version history."
    },
    {
        'id': 38,
        'question': "What is a primary key that consists of two or more attributes called?",
        'options': [
            'A. Foreign Key',
            'B. Composite Key',
            'C. Super Key',
            'D. Secondary Key',
            'E. Unique Key'
        ],
        'correct_answer': 'B. Composite Key',
        'explanation': "A composite key combines two or more table columns to uniquely identify table rows."
    },
    {
        'id': 39,
        'question': "Which algorithm design strategy breaks a problem into smaller subproblems, solves them recursively, and combines their solutions?",
        'options': [
            'A. Greedy Approach',
            'B. Dynamic Programming',
            'C. Divide and Conquer',
            'D. Backtracking',
            'E. Brute Force'
        ],
        'correct_answer': 'C. Divide and Conquer',
        'explanation': "Divide and conquer recursively splits problems into independent subproblems, solves them, and merges results (e.g., Merge Sort)."
    },
    {
        'id': 40,
        'question': "What is the function of the ARP protocol in computer networking?",
        'options': [
            'A. Translates logical IP addresses into physical MAC addresses',
            'B. Automatically assigns host configuration parameters',
            'C. Resolves human-readable domain names into IP addresses',
            'D. Establishes encrypted VPN tunnels',
            'E. Manages routing tables'
        ],
        'correct_answer': 'A. Translates logical IP addresses into physical MAC addresses',
        'explanation': "ARP matches network layer IP addresses with data link layer MAC addresses."
    },
    {
        'id': 41,
        'question': "Which cybersecurity attack tricks users into revealing confidential credentials by pretending to be a trustworthy entity via email?",
        'options': [
            'A. Spoofing',
            'B. Phishing',
            'C. Sniffing',
            'D. Ransomware',
            'E. Rootkit'
        ],
        'correct_answer': 'B. Phishing',
        'explanation': "Phishing uses deceptive emails or messages disguised as legitimate entities to harvest sensitive user credentials."
    },
    {
        'id': 42,
        'question': "Which SDLC phase involves converting user requirement specifications into actual executable source code?",
        'options': [
            'A. Requirement Analysis',
            'B. System Design',
            'C. Implementation (Coding)',
            'D. Maintenance',
            'E. Testing'
        ],
        'correct_answer': 'C. Implementation (Coding)',
        'explanation': "During the implementation phase, developers write code and build software modules according to design specifications."
    },
    {
        'id': 43,
        'question': "Which command in Linux displays current active network connections and listening ports?",
        'options': [
            'A. ifconfig',
            'B. netstat',
            'C. ping',
            'D. traceroute',
            'E. ipconfig'
        ],
        'correct_answer': 'B. netstat',
        'explanation': "'netstat' inspects network connections, routing tables, and interface statistics on operating systems."
    },
    {
        'id': 44,
        'question': "What does ACID stand for in DBMS transaction processing?",
        'options': [
            'A. Atomicity, Consistency, Isolation, Durability',
            'B. Accuracy, Control, Integrity, Dependability',
            'C. Availability, Concurrency, Indexing, Data',
            'D. Access, Communication, Integration, Distribution',
            'E. Authentication, Confidentiality, Integrity, Delivery'
        ],
        'correct_answer': 'A. Atomicity, Consistency, Isolation, Durability',
        'explanation': "ACID properties ensure reliable and predictable database transactions."
    },
    {
        'id': 45,
        'question': "Which type of database stores data in key-value pairs, documents, or wide-column stores without rigid schemas?",
        'options': [
            'A. Relational Database',
            'B. NoSQL Database',
            'C. Hierarchical Database',
            'D. Network Database',
            'E. Object-Relational Database'
        ],
        'correct_answer': 'B. NoSQL Database',
        'explanation': "NoSQL databases provide flexible schema designs for distributed unstructured or semi-structured data models."
    },
    {
        'id': 46,
        'question': "Which OOP concept refers to restricting direct access to some of an object's components and hiding internal implementation details?",
        'options': [
            'A. Polymorphism',
            'B. Inheritance',
            'C. Encapsulation',
            'D. Abstraction',
            'E. Overloading'
        ],
        'correct_answer': 'C. Encapsulation',
        'explanation': "Encapsulation bundles data and methods into a single unit while hiding internal state details using access modifiers."
    },
    {
        'id': 47,
        'question': "In human-computer interaction (HCI), what does 'Usability' primarily refer to?",
        'options': [
            'A. The speed of the server hosting the software',
            'B. The ease of learning, efficiency, and satisfaction for users interacting with a system',
            'C. The security level of user password hashes',
            'D. The graphical resolution of user interface icons',
            'E. The size of the application codebase'
        ],
        'correct_answer': 'B. The ease of learning, efficiency, and satisfaction for users interacting with a system',
        'explanation': "Usability evaluates how intuitively, efficiently, and satisfactorily users can interact with software systems."
    },
    {
        'id': 48,
        'question': "Which network protocol is connectionless and does not guarantee reliable delivery of data packets?",
        'options': [
            'A. TCP',
            'B. UDP',
            'C. HTTP',
            'D. SSH',
            'E. FTP'
        ],
        'correct_answer': 'B. UDP',
        'explanation': "User Datagram Protocol (UDP) is connectionless, prioritizing speed over delivery guarantees or error correction."
    },
    {
        'id': 49,
        'question': "What is a 'Firewall' in network security?",
        'options': [
            'A. An antivirus scanner installed on client workstations',
            'B. A device or software that monitors and controls network traffic based on security rules',
            'C. A physical backup server placed in a remote datacenter',
            'D. A protocol used to assign dynamic IP addresses',
            'E. A hardware component for wireless signal boosting'
        ],
        'correct_answer': 'B. A device or software that monitors and controls network traffic based on security rules',
        'explanation': "Firewalls inspect incoming and outgoing network traffic to block unauthorized access based on predefined security rules."
    },
    {
        'id': 50,
        'question': "What is the worst-case time complexity of the Bubble Sort algorithm?",
        'options': [
            'A. O(1)',
            'B. O(log n)',
            'C. O(n)',
            'D. O(n²)',
            'E. O(n log n)'
        ],
        'correct_answer': 'D. O(n²)',
        'explanation': "Bubble sort compares adjacent elements iteratively, leading to quadratic O(n²) worst-case time complexity."
    },
    {
        'id': 51,
        'question': "Which device operates at Layer 3 (Network Layer) of the OSI model?",
        'options': [
            'A. Hub',
            'B. Switch',
            'C. Router',
            'D. Repeater',
            'E. Bridge'
        ],
        'correct_answer': 'C. Router',
        'explanation': "Routers operate at Layer 3 to route data packets across disparate networks using IP addresses."
    },
    {
        'id': 52,
        'question': "In SQL, which clause is used to filter records after an aggregate operation (e.g., after GROUP BY)?",
        'options': [
            'A. WHERE',
            'B. HAVING',
            'C. ORDER BY',
            'D. LIKE',
            'E. LIMIT'
        ],
        'correct_answer': 'B. HAVING',
        'explanation': "HAVING filters grouped rows resulting from aggregation, whereas WHERE filters rows before grouping."
    },
    {
        'id': 53,
        'question': "What is the main characteristic of a peer-to-peer (P2P) network architecture?",
        'options': [
            'A. A central server manages all network requests and authentication',
            'B. Each node can act as both a client and a server',
            'C. All traffic flows through a dedicated main controller',
            'D. It relies exclusively on fiber-optic physical media',
            'E. Only one device can transmit at any given time'
        ],
        'correct_answer': 'B. Each node can act as both a client and a server',
        'explanation': "In a P2P network, participating nodes share workloads and act simultaneously as clients and servers."
    },
    {
        'id': 54,
        'question': "Which software testing methodology tests individual components or modules in isolation?",
        'options': [
            'A. System Testing',
            'B. Integration Testing',
            'C. Unit Testing',
            'D. Acceptance Testing',
            'E. Regression Testing'
        ],
        'correct_answer': 'C. Unit Testing',
        'explanation': "Unit testing verifies individual software components, functions, or classes in isolation."
    },
    {
        'id': 55,
        'question': "What type of malware encrypts a user's files and demands payment to restore access?",
        'options': [
            'A. Spyware',
            'B. Ransomware',
            'C. Adware',
            'D. Keylogger',
            'E. Trojan'
        ],
        'correct_answer': 'B. Ransomware',
        'explanation': "Ransomware locks or encrypts victims' files and demands financial ransom for the decryption key."
    },
    {
        'id': 56,
        'question': "In Data Structures, which traversal method visits the nodes of a binary tree in the order: Left, Root, Right?",
        'options': [
            'A. Pre-order Traversal',
            'B. In-order Traversal',
            'C. Post-order Traversal',
            'D. Level-order Traversal',
            'E. Breadth-First Search'
        ],
        'correct_answer': 'B. In-order traversal',
        'explanation': "In-order traversal visits the left subtree, then the root node, and finally the right subtree."
    },
    {
        'id': 57,
        'question': "Which protocol is primarily used to send emails between servers across the Internet?",
        'options': [
            'A. POP3',
            'B. IMAP',
            'C. SMTP',
            'D. FTP',
            'E. HTTP'
        ],
        'correct_answer': 'C. SMTP',
        'explanation': "Simple Mail Transfer Protocol (SMTP) handles email transmission between mail servers."
    },
    {
        'id': 58,
        'question': "What is the process of converting readable plain text into unreadable ciphertext called?",
        'options': [
            'A. Decryption',
            'B. Encryption',
            'C. Hashing',
            'D. Compression',
            'E. Encoding'
        ],
        'correct_answer': 'B. Encryption',
        'explanation': "Encryption scrambles plaintext data into ciphertext using cryptographic algorithms and keys."
    },
    {
        'id': 59,
        'question': "In Object-Oriented Programming, creating multiple methods in the same class with the same name but different parameters is called:",
        'options': [
            'A. Method Overriding',
            'B. Method Overloading',
            'C. Inheritance',
            'D. Dynamic Binding',
            'E. Encapsulation'
        ],
        'correct_answer': 'B. Method Overloading',
        'explanation': "Method overloading permits multiple methods with identical names but distinct parameter signatures within a class."
    },
    {
        'id': 60,
        'question': "Which SQL command is used to remove a table and all its data permanently from a database?",
        'options': [
            'A. DELETE TABLE',
            'B. REMOVE TABLE',
            'C. DROP TABLE',
            'D. TRUNCATE DATABASE',
            'E. CLEAR TABLE'
        ],
        'correct_answer': 'C. DROP TABLE',
        'explanation': "The DROP TABLE command completely deletes a table definition, indexes, and all stored data from the database."
    },
    {
        'id': 61,
        'question': "What is Virtual Memory in an Operating System?",
        'options': [
            'A. RAM installed on a graphics display card',
            'B. A memory management technique that uses secondary storage to extend physical RAM',
            'C. Fast cache memory built directly into the CPU core',
            'D. Read-Only Memory used during the system boot process',
            'E. Cloud-hosted RAM partitions'
        ],
        'correct_answer': 'B. A memory management technique that uses secondary storage to extend physical RAM',
        'explanation': "Virtual memory uses disk space (swap space/page file) to give applications the illusion of larger contiguous RAM."
    },
    {
        'id': 62,
        'question': "Which topology provides the highest level of redundancy and fault tolerance?",
        'options': [
            'A. Star Topology',
            'B. Mesh Topology',
            'C. Ring Topology',
            'D. Bus Topology',
            'E. Tree Topology'
        ],
        'correct_answer': 'B. Mesh Topology',
        'explanation': "In a full mesh topology, every node connects to multiple nodes, ensuring maximum fault tolerance and redundant paths."
    },
    {
        'id': 63,
        'question': "What does CSS stand for in web development?",
        'options': [
            'A. Creative Style Sheets',
            'B. Cascading Style Sheets',
            'C. Computer Style System',
            'D. Custom Sheet Software',
            'E. Colorful Style Sheets'
        ],
        'correct_answer': 'B. Cascading Style Sheets',
        'explanation': "CSS stands for Cascading Style Sheets, used to format the visual presentation of web documents."
    },
    {
        'id': 64,
        'question': "Which layer of the OSI model handles data compression, encryption, and formatting?",
        'options': [
            'A. Application Layer',
            'B. Presentation Layer',
            'C. Session Layer',
            'D. Transport Layer',
            'E. Data Link Layer'
        ],
        'correct_answer': 'B. Presentation Layer',
        'explanation': "The Presentation Layer (Layer 6) translates data formats, handles encryption/decryption, and manages data compression."
    },
    {
        'id': 65,
        'question': "In a relational database, what is a 'Foreign Key'?",
        'options': [
            'A. A key imported from an external non-SQL database',
            'B. An attribute in one table that uniquely references a primary key in another table',
            'C. A primary key containing text instead of numerical values',
            'D. An automatically generated unique index number',
            'E. A temporary decryption key'
        ],
        'correct_answer': 'B. An attribute in one table that uniquely references a primary key in another table',
        'explanation': "A foreign key links records across tables by referencing the primary key of a parent table."
    },
    {
        'id': 66,
        'question': "What is the main purpose of a Subnet Mask in IP networking?",
        'options': [
            'A. To translate host domain names into physical MAC addresses',
            'B. To distinguish the network portion of an IP address from the host portion',
            'C. To encrypt data packets transmitted over wireless networks',
            'D. To assign dynamic IP addresses automatically',
            'E. To prioritize voice traffic over video'
        ],
        'correct_answer': 'B. To distinguish the network portion of an IP address from the host portion',
        'explanation': "A subnet mask partitions an IP address into its network identifier and host identifier components."
    },
    {
        'id': 67,
        'question': "Which scheduling algorithm can lead to 'Starvation' for lower-priority tasks?",
        'options': [
            'A. Round Robin',
            'B. Priority Scheduling',
            'C. First-Come, First-Served',
            'D. Shortest Job First (Non-preemptive)',
            'E. Multilevel Feedback Queue with aging'
        ],
        'correct_answer': 'B. Priority Scheduling',
        'explanation': "Priority scheduling can starve lower-priority processes indefinitely if higher-priority processes keep arriving."
    },
    {
        'id': 68,
        'question': "In software design, what does the term 'Coupling' measure?",
        'options': [
            'A. The degree of interdependence between different software modules',
            'B. The internal strength and focus of a single module's tasks',
            'C. The speed of execution of database queries',
            'D. The total lines of source code in a project',
            'E. Hardware resource utilization'
        ],
        'correct_answer': 'A. The degree of interdependence between different software modules',
        'explanation': "Coupling measures how tightly connected or dependent separate software modules are on one another."
    },
    {
        'id': 69,
        'question': "Which type of database join returns all records from the left table and matching records from the right table?",
        'options': [
            'A. INNER JOIN',
            'B. LEFT JOIN',
            'C. RIGHT JOIN',
            'D. FULL OUTER JOIN',
            'E. CROSS JOIN'
        ],
        'correct_answer': 'B. LEFT JOIN',
        'explanation': "A LEFT JOIN returns all rows from the left table, along with matching rows from the right table (or NULLs if no match)."
    },
    {
        'id': 70,
        'question': "What is a 'MAC Address'?",
        'options': [
            'A. A logical address assigned dynamically by a router',
            'B. A hardware address permanently burned into a Network Interface Card (NIC)',
            'C. A temporary IP address assigned to mobile clients',
            'D. A domain name assigned to local network servers',
            'E. An encrypted wireless key'
        ],
        'correct_answer': 'B. A hardware address permanently burned into a Network Interface Card (NIC)',
        'explanation': "A Media Access Control (MAC) address is a unique hardware identifier assigned to network interfaces at the factory."
    },
    {
        'id': 71,
        'question': "Which cloud service model allows developers to build and deploy applications without managing underlying servers (e.g., Firebase, AWS Elastic Beanstalk)?",
        'options': [
            'A. IaaS',
            'B. PaaS',
            'C. SaaS',
            'D. DaaS',
            'E. BaaS'
        ],
        'correct_answer': 'B. PaaS',
        'explanation': "Platform as a Service (PaaS) provides managed environments and frameworks so developers can focus solely on writing code."
    },
    {
        'id': 72,
        'question': "What is the time complexity of pushing an element onto a Stack data structure?",
        'options': [
            'A. O(1)',
            'B. O(log n)',
            'C. O(n)',
            'D. O(n²)',
            'E. O(n log n)'
        ],
        'correct_answer': 'A. O(1)',
        'explanation': "Pushing an element onto a stack takes constant time O(1) when inserting at the head/top."
    },
    {
        'id': 73,
        'question': "Which vulnerability allows an attacker to execute malicious scripts in a victim's web browser?",
        'options': [
            'A. SQL Injection',
            'B. Cross-Site Scripting (XSS)',
            'C. Buffer Overflow',
            'D. IP Spoofing',
            'E. Session Fixation'
        ],
        'correct_answer': 'B. Cross-Site Scripting (XSS)',
        'explanation': "XSS injects malicious client-side scripts (usually JavaScript) into trusted websites viewed by other users."
    },
    {
        'id': 74,
        'question': "What is the primary role of the DHCP server in a network?",
        'options': [
            'A. Resolving domain names to IP addresses',
            'B. Automatically assigning IP addresses and network configuration to hosts',
            'C. Filtering malicious network packets',
            'D. Mirroring server data for disaster recovery',
            'E. Monitoring link bandwidth'
        ],
        'correct_answer': 'B. Automatically assigning IP addresses and network configuration to hosts',
        'explanation': "Dynamic Host Configuration Protocol (DHCP) servers dynamically distribute IP addresses and gateway configs to devices."
    },
    {
        'id': 75,
        'question': "Which software architecture divides an application into Model, View, and Controller layers?",
        'options': [
            'A. Monolithic Architecture',
            'B. Microservices Architecture',
            'C. MVC Architecture',
            'D. Peer-to-Peer Architecture',
            'E. Event-Driven Architecture'
        ],
        'correct_answer': 'C. MVC Architecture',
        'explanation': "Model-View-Controller separates business logic (Model), UI presentation (View), and user input handling (Controller)."
    },
    {
        'id': 76,
        'question': "Which sorting algorithm uses a 'Pivot' element to partition an array into smaller sub-arrays?",
        'options': [
            'A. Insertion Sort',
            'B. Quick Sort',
            'C. Selection Sort',
            'D. Bubble Sort',
            'E. Heap Sort'
        ],
        'correct_answer': 'B. Quick Sort',
        'explanation': "Quicksort selects a pivot value and partitions elements around it recursively."
    },
    {
        'id': 77,
        'question': "In Version Control Systems (Git), what is the purpose of git status?",
        'options': [
            'A. Displays the history of all commits',
            'B. Shows the working directory and staging area state',
            'C. Uploads local commits to a remote server',
            'D. Merges two development branches',
            'E. Creates a new branch'
        ],
        'correct_answer': 'B. Shows the working directory and staging area state',
        'explanation': "'git status' reports which files are staged, unstaged, or untracked in the working repository."
    },
    {
        'id': 78,
        'question': "Which HTTP method is typically used to update an existing resource on a web server?",
        'options': [
            'A. GET',
            'B. POST',
            'C. PUT',
            'D. DELETE',
            'E. OPTIONS'
        ],
        'correct_answer': 'C. PUT',
        'explanation': "PUT requests are typically used in RESTful APIs to update or replace an existing resource completely."
    },
    {
        'id': 79,
        'question': "What type of attack involves manipulating input fields to execute arbitrary database queries?",
        'options': [
            'A. Cross-Site Scripting',
            'B. SQL Injection',
            'C. Man-in-the-Middle',
            'D. Brute Force',
            'E. Credential Stuffing'
        ],
        'correct_answer': 'B. SQL Injection',
        'explanation': "SQL Injection exploits insecure input validation to insert malicious SQL statements into database queries."
    },
    {
        'id': 80,
        'question': "In Operating Systems, what is 'Thrashing'?",
        'options': [
            'A. Rapid switching between user space and kernel space',
            'B. Excessive swapping of pages between RAM and disk, causing performance drop',
            'C. Simultaneous execution of CPU-bound threads',
            'D. Unintended deletion of system log files',
            'E. Processor overheating due to heavy computation'
        ],
        'correct_answer': 'B. Excessive swapping of pages between RAM and disk, causing performance drop',
        'explanation': "Thrashing occurs when an OS spends more time paging data to disk than executing actual instructions."
    },
    {
        'id': 81,
        'question': "Which transmission medium transmits data using light signals through glass or plastic fibers?",
        'options': [
            'A. Unshielded Twisted Pair (UTP)',
            'B. Coaxial Cable',
            'C. Fiber Optic Cable',
            'D. Shielded Twisted Pair (STP)',
            'E. Infrared Waves'
        ],
        'correct_answer': 'C. Fiber Optic Cable',
        'explanation': "Fiber optic cables carry data over long distances at high speeds via pulses of light through glass/plastic fibers."
    },
    {
        'id': 82,
        'question': "What is the primary function of an Index in a DBMS?",
        'options': [
            'A. To enforce referential integrity between tables',
            'B. To speed up data retrieval operations on a database table',
            'C. To compress stored text data',
            'D. To encrypt column values automatically',
            'E. To log user transaction histories'
        ],
        'correct_answer': 'B. To speed up data retrieval operations on a database table',
        'explanation': "Database indexes provide rapid lookup paths to rows, greatly accelerating query execution speeds."
    },
    {
        'id': 83,
        'question': "In Agile development, what is a 'Sprint'?",
        'options': [
            'A. A rapid bug-fixing session held right before deployment',
            'B. A set, short period of time during which specific work must be completed',
            'C. A hardware testing phase performed by end users',
            'D. An emergency patch deployed directly to production',
            'E. A daily standup meeting'
        ],
        'correct_answer': 'B. A set, short period of time during which specific work must be completed',
        'explanation': "A sprint is a fixed time-box (typically 1–4 weeks) in Scrum where a specific chunk of product backlog items is built."
    },
    {
        'id': 84,
        'question': "Which cryptographic function produces a fixed-length string regardless of input size and is non-reversible?",
        'options': [
            'A. Symmetric Encryption',
            'B. Asymmetric Encryption',
            'C. Hash Function',
            'D. Steganography',
            'E. Base64 Encoding'
        ],
        'correct_answer': 'C. Hash Function',
        'explanation': "Cryptographic hash functions (like SHA-256) generate fixed-size outputs and are computationally irreversible."
    },
    {
        'id': 85,
        'question': "What does the ping network command measure?",
        'options': [
            'A. Server bandwidth capacity',
            'B. Network round-trip time and host reachability',
            'C. Available memory on a target system',
            'D. Active database user sessions',
            'E. Packet loss percentage only'
        ],
        'correct_answer': 'B. Network round-trip time and host reachability',
        'explanation': "Ping uses ICMP echo requests to verify network connectivity and measure round-trip travel time."
    },
    {
        'id': 86,
        'question': "Which software process model combines iterative development with systematic risk assessment?",
        'options': [
            'A. Waterfall Model',
            'B. Spiral Model',
            'C. V-Model',
            'D. Rapid Application Development (RAD)',
            'E. Big Bang Model'
        ],
        'correct_answer': 'B. Spiral Model',
        'explanation': "The Spiral model integrates iterative prototyping features with rigorous, systematic risk analysis phases."
    },
    {
        'id': 87,
        'question': "In Object-Oriented Programming, what is 'Polymorphism'?",
        'options': [
            'A. Hiding sensitive data fields inside a class',
            'B. The ability of different classes to respond to the same method call in unique ways',
            'C. Restricting class instantiation to a single object instance',
            'D. Reusing class code through parent-child relationships',
            'E. Multiple inheritance of interfaces'
        ],
        'correct_answer': 'B. The ability of different classes to respond to the same method call in unique ways',
        'explanation': "Polymorphism allows objects of different classes to be treated through the same common interface, exhibiting unique behaviors."
    },
    {
        'id': 88,
        'question': "Which wireless security protocol is considered the most secure for Wi-Fi networks today?",
        'options': [
            'A. WEP',
            'B. WPA',
            'C. WPA2 / WPA3',
            'D. TKIP',
            'E. MAC Filtering'
        ],
        'correct_answer': 'C. WPA2 / WPA3',
        'explanation': "WPA2 and WPA3 provide robust modern encryption standards (such as AES) for securing wireless networks."
    },
    {
        'id': 89,
        'question': "What is the primary purpose of a Proxy Server?",
        'options': [
            'A. To convert source code into machine code',
            'B. To act as an intermediary between client requests and target servers for security or caching',
            'C. To allocate dynamic IP addresses automatically',
            'D. To perform database query optimization',
            'E. To manage physical fiber connections'
        ],
        'correct_answer': 'B. To act as an intermediary between client requests and target servers for security or caching',
        'explanation': "Proxy servers intermediate client requests, providing caching, filtering, and anonymity."
    },
    {
        'id': 90,
        'question': "In Software Engineering, what does 'Cohesion' refer to?",
        'options': [
            'A. How strongly related and focused the responsibilities within a single module are',
            'B. The total number of dependencies between distinct system modules',
            'C. The speed at which code compiles',
            'D. The process of connecting database tables using primary keys',
            'E. Code reusability across platforms'
        ],
        'correct_answer': 'A. How strongly related and focused the responsibilities within a single module are',
        'explanation': "High cohesion means a single module performs a single, well-defined task with tightly related functions."
    },
    {
        'id': 91,
        'question': "Which protocol is used to securely transfer files over an encrypted SSH connection?",
        'options': [
            'A. FTP',
            'B. TFTP',
            'C. SFTP',
            'D. HTTP',
            'E. SMTP'
        ],
        'correct_answer': 'C. SFTP',
        'explanation': "SSH File Transfer Protocol (SFTP) provides secure file transmission capabilities over reliable SSH tunnels."
    },
    {
        'id': 92,
        'question': "What is a 'Zombie' or 'Botnet' computer in cybersecurity?",
        'options': [
            'A. A server with outdated firmware',
            'B. A compromised computer controlled remotely to participate in malicious attacks',
            'C. A system running isolated virtual machines',
            'D. A workstation lacking an activated antivirus license',
            'E. A crashed system awaiting reboot'
        ],
        'correct_answer': 'B. A compromised computer controlled remotely to participate in malicious attacks',
        'explanation': "Botnets consist of infected zombie computers remotely controlled by attackers to execute coordinated distributed attacks."
    },
    {
        'id': 93,
        'question': "Which type of testing evaluates whether new code changes break existing functionality?",
        'options': [
            'A. Unit Testing',
            'B. Regression Testing',
            'C. Stress Testing',
            'D. Smoke Testing',
            'E. Alpha Testing'
        ],
        'correct_answer': 'B. Regression Testing',
        'explanation': "Regression testing re-runs functional and non-functional tests to ensure code updates haven't broken existing features."
    },
    {
        'id': 94,
        'question': "What is the binary representation of the decimal number 10?",
        'options': [
            'A. 1001',
            'B. 1010',
            'C. 1100',
            'D. 1110',
            'E. 1111'
        ],
        'correct_answer': 'B. 1010',
        'explanation': "Decimal 10 equals 8 + 2, represented in binary as 1010 ($2^3 + 2^1$). "
    },
    {
        'id': 95,
        'question': "In DBMS, what does the COMMIT transaction control command do?",
        'options': [
            'A. Undoes all changes made during the current transaction',
            'B. Saves all changes made during the transaction permanently to the database',
            'C. Temporarily pauses query execution',
            'D. Deletes all rollback segments',
            'E. Locks the active table'
        ],
        'correct_answer': 'B. Saves all changes made during the transaction permanently to the database',
        'explanation': "COMMIT makes all modifications performed during the current transaction permanent."
    },
    {
        'id': 96,
        'question': "Which Linux command is used to display currently running processes?",
        'options': [
            'A. ls',
            'B. top / ps',
            'C. pwd',
            'D. df',
            'E. du'
        ],
        'correct_answer': 'B. top / ps',
        'explanation': "'ps' and 'top' commands list and monitor active processes running on Linux operating systems."
    },
    {
        'id': 97,
        'question': "What is the default port number used by HTTPS?",
        'options': [
            'A. 80',
            'B. 21',
            'C. 443',
            'D. 22',
            'E. 8080'
        ],
        'correct_answer': 'C. 443',
        'explanation': "Secure HTTPS web traffic defaults to TCP port 443."
    },
    {
        'id': 98,
        'question': "What is the primary goal of Continuous Integration (CI) in DevOps?",
        'options': [
            'A. To eliminate the need for automated unit tests',
            'B. To frequently merge developer code changes into a central repository and run automated builds/tests',
            'C. To manage cloud infrastructure billing automatically',
            'D. To replace traditional relational databases with NoSQL',
            'E. To automate customer support tickets'
        ],
        'correct_answer': 'B. To frequently merge developer code changes into a central repository and run automated builds/tests',
        'explanation': "Continuous Integration regularly merges developer changes into main branches, testing builds automatically to detect integration errors early."
    },
    {
        'id': 99,
        'question': "Which data structure is non-linear and consists of nodes connected by edges without closed cycles?",
        'options': [
            'A. Queue',
            'B. Tree',
            'C. Linked List',
            'D. Array',
            'E. Stack'
        ],
        'correct_answer': 'B. Tree',
        'explanation': "A tree is a hierarchical, non-linear data structure consisting of connected nodes without cycles."
    },
    {
        'id': 100,
        'question': "In computer architecture, what is 'Pipelining'?",
        'options': [
            'A. Storing multiple copies of web pages on remote caching servers',
            'B. A technique where multiple instruction execution steps are overlapped in time',
            'C. Connecting multiple hard drives together using RAID configurations',
            'D. Encrypting data streams sent across wireless routers',
            'E. Transferring files over SSH'
        ],
        'correct_answer': 'B. A technique where multiple instruction execution steps are overlapped in time',
        'explanation': "Pipelining overlaps instruction processing steps in the CPU datapath to increase instruction throughput."
    }
]
