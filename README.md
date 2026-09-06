# Networks

![Course](https://img.shields.io/badge/course-Networks-1f6feb?style=for-the-badge)
![Language](https://img.shields.io/badge/materials-English-2ea44f?style=for-the-badge)
![Python](https://img.shields.io/badge/labs-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Course notes, demonstrations, laboratories, and exercises for **Computer Networks**, based on *Computer Networking: A Top-Down Approach*. The course is taught in English and combines protocol theory with practical Python networking experiments.

The complete 2026 course workspace is maintained in [Notion](https://upbeat-beef-3ff.notion.site/2026-Networks-2f5915764eda8021b53bd94c381ea78c). This repository contains the code and notebooks that support the lectures and laboratories.

## Course Overview

The course follows a top-down view of computer networks: we begin with the applications people use, then study the transport and network layers, move down to links and wireless communication, and finish with security.

The repository is organized by course unit. Each unit contains the code, notebooks, and activities used in class. The Notion workspace contains the current schedule, instructions, submissions, lecture resources, and assessment information.

## Contents

- [Learning Goals](#learning-goals)
- [Course Units](#course-units)
- [Course Policies and Methodology](#course-policies-and-methodology)
- [Assessment](#assessment)
- [Exams and Project](#exams-and-project)
- [Books and References](#books-and-references)
- [Tools](#tools)
- [Other Resources](#other-resources)
- [Repository Structure](#repository-structure)

## Learning Goals

By the end of the course, students should be able to:

- Explain how protocols and layered architectures make the Internet work.
- Analyze application, transport, network, link, and wireless-layer behavior.
- Build client-server applications using TCP, UDP, HTTP, and SMTP.
- Use Python to inspect, test, and automate networked systems.
- Compare reliability, congestion control, routing, switching, and medium-access mechanisms.
- Identify common network threats and apply basic defensive techniques.

## Course Policies and Methodology

- [Course policies](https://upbeat-beef-3ff.notion.site/Course-Policies-2f5915764eda8146b8f0f1356bcdb869?pvs=25) and academic regulations apply to all course activities.
- Lectures introduce the concepts and protocols; laboratories use Wireshark, AWS, Cisco Packet Tracer, Huawei ICT Academy, Python, and Docker to connect theory with practice.
- Laboratory work is submitted through Moodle according to the deadlines announced in Notion. Completed work may need to be presented to the instructor before grading.
- The Wireshark activities are based on the [official Kurose and Ross Wireshark labs](http://gaia.cs.umass.edu/kurose_ross/wireshark.php).
- The course workspace uses English for lectures, instructions, code, and technical submissions.

## Course Units

### Unit 1. Computer Networks and the Internet

**Topics:** The Internet as a network of networks, end systems, access networks, packet switching, protocol layers, delay, loss, throughput, and network security foundations.

**Chapter:** 1, *Computer Networks and the Internet*

[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/Networks/tree/main/1.%20Computer%20Networks%20and%20The%20Internet)
[![Canva Slides](https://img.shields.io/badge/Canva-slides-7D2AE8?logo=canva&logoColor=white)](#)
[![Notion Lecture](https://img.shields.io/badge/Notion-lecture-37352F?logo=notion&logoColor=white)](https://upbeat-beef-3ff.notion.site/Lecture-slides-Computer-Networks-and-the-Internet-2f5915764eda81f8bff9c363e346dce8?pvs=25)

**Laboratory:** [Lab 1: Getting Started with Wireshark](https://upbeat-beef-3ff.notion.site/Lab-1-Getting-Started-with-Wireshark-2f5915764eda81e49cc0d2a91c6fa95a?pvs=25)

> Submit a PDF through Moodle and present the work to the instructor. The lab deadline is announced in Notion.

### Unit 2. The Application Layer

**Topics:** Principles of network applications, the Web and HTTP, electronic mail and SMTP, DNS, socket programming, and application-layer protocols.

**Chapter:** 2, *The Application Layer*

[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/Networks/tree/main/2.%20The%20Application%20Layer)
[![Canva Slides](https://img.shields.io/badge/Canva-slides-7D2AE8?logo=canva&logoColor=white)](#)
[![Notion Lecture](https://img.shields.io/badge/Notion-lecture-37352F?logo=notion&logoColor=white)](https://upbeat-beef-3ff.notion.site/Lecture-slides-Application-Layer-2f5915764eda81ec9cdceef9ab97e9a7?pvs=25)

**Materials:**

- [HTTP web server with FastAPI](2.%20The%20Application%20Layer/http-web-server-with-FastAPI)
- [SMTP examples](2.%20The%20Application%20Layer/smtp)
- [TCP application-layer lab](2.%20The%20Application%20Layer/tcp-lab)
- [Lab 2.1: HTTP (Wireshark)](https://upbeat-beef-3ff.notion.site/Lab-2-1-HTTP-Wireshark-2f5915764eda816ba2dfea850fda1b82?pvs=25)
- [Lab 2.2: ICMP on AWS EC2](https://upbeat-beef-3ff.notion.site/Lab-2-2-ICMP-on-AWS-EC2-2f5915764eda81b4af6bcb24c9ccdbb2?pvs=25)
- [AWS EC2 creation and SSH from Linux](https://upbeat-beef-3ff.notion.site/AWS-EC2-Instance-Creation-and-SSH-Access-from-Linux-2f5915764eda815f8f06c9339960dbaa?pvs=25)
- [Huawei Cloud Flexus ECS instance creation](https://upbeat-beef-3ff.notion.site/Huawei-Cloud-Flexus-ECS-Instance-creation-315915764eda80029e2dee65b80531cc?pvs=25)

> **Slides:** Add the Canva presentation link here.

### Unit 3. The Transport Layer

**Topics:** Multiplexing and demultiplexing, UDP, reliable data transfer, TCP, flow control, connection management, and congestion control.

**Chapter:** 3, *The Transport Layer*

[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/Networks/tree/main/3.%20Transport%20Layer)
[![Canva Slides](https://img.shields.io/badge/Canva-slides-7D2AE8?logo=canva&logoColor=white)](#)
[![Notion Lecture](https://img.shields.io/badge/Notion-lecture-37352F?logo=notion&logoColor=white)](https://upbeat-beef-3ff.notion.site/Lecture-slides-Transport-Layer-2f5915764eda81fd9f06dcc92516d290?pvs=25)

**Materials:**

- [Calculator client-server](3.%20Transport%20Layer/calculator)
- [TCP client and server](3.%20Transport%20Layer/tcp)
- [Threaded client and server](3.%20Transport%20Layer/threads)
- [UDP exercises](3.%20Transport%20Layer/udp)
- [Automatic testing scripts](3.%20Transport%20Layer/auto_testing_scripts)
- [Lab 3.1: UDP (Wireshark)](https://upbeat-beef-3ff.notion.site/Lab-3-1-UDP-Wireshark-2f5915764eda8111b642fc2b3507881c?pvs=25)
- [Lab 3.2: TCP (Wireshark)](https://upbeat-beef-3ff.notion.site/Lab-3-2-TCP-Wireshark-2f5915764eda810bbc5ad6ccd0a0792a?pvs=25)
- [Lab 3.3: Handling errors with sockets on AWS](https://upbeat-beef-3ff.notion.site/Lab-3-3-Handling-errors-with-Sockets-AWS-2f5915764eda81ff948cf33a06035abf?pvs=25)

> **Slides:** Add the Canva presentation link here.

### Unit 4. The Network Layer: Data Plane

**Topics:** Network-layer services, forwarding, routing tables, Internet Protocol, addressing, router architecture, and generalized forwarding.

**Chapter:** 4, *The Network Layer: Data Plane*

[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/Networks/tree/main/4.%20The%20Network%20Layer%3A%20Data%20Plane)
[![Canva Slides](https://img.shields.io/badge/Canva-slides-7D2AE8?logo=canva&logoColor=white)](#)
[![Notion Lecture](https://img.shields.io/badge/Notion-lecture-37352F?logo=notion&logoColor=white)](https://upbeat-beef-3ff.notion.site/Lecture-slides-The-Network-Layer-Data-Plane-2f5915764eda81d38c42e5771bb42504?pvs=25)

**Notion laboratories:**

- [Lab 4.1: Getting started with Cisco Packet Tracer](https://upbeat-beef-3ff.notion.site/Lab-4-1-Getting-started-with-CISCO-Packet-Tracer-NetAcad-Course-2f5915764eda81b18ab5c9f8647a0d02?pvs=25)
- [Lab 4.2: Local Area Network with Cisco Packet Tracer](https://upbeat-beef-3ff.notion.site/Lab-4-2-Local-Area-Network-LAN-CISCO-Packet-Tracer-2f5915764eda81bf9f41d89812b711b8?pvs=25)
- Lab 4.3: Threaded server on AWS (not required)

> **Slides:** Add the Canva presentation link here.

### Unit 5. The Network Layer: Control Plane

**Topics:** Routing algorithms, intra-AS and inter-AS routing, OSPF, BGP, SDN control, and network management.

**Chapter:** 5, *The Network Layer: Control Plane*

[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/Networks/tree/main/5.%20The%20Network%20Layer%3A%20Control%20Plane)
[![Canva Slides](https://img.shields.io/badge/Canva-slides-7D2AE8?logo=canva&logoColor=white)](#)
[![Notion Lecture](https://img.shields.io/badge/Notion-lecture-37352F?logo=notion&logoColor=white)](https://upbeat-beef-3ff.notion.site/Lecture-slides-The-Network-Layer-Control-Plane-2f5915764eda81b4a0fccb07e0344435?pvs=25)

**Notion laboratory:** [Lab 5.1: Dynamic Routing Algorithm (RIP) with Cisco Packet Tracer](https://upbeat-beef-3ff.notion.site/Lab-5-1-Dynamic-Routing-Algorithm-RIP-CISCO-Packet-Tracer-2f5915764eda8122ae39cbc34fc3a27c?pvs=25)

> **Slides:** Add the Canva presentation link here.

### Unit 6. The Link Layer and LANs

**Topics:** Error detection and correction, multiple access protocols, Ethernet, switched LANs, VLANs, data-center networking, and link virtualization.

**Chapter:** 6, *The Link Layer and LANs*

[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/Networks/tree/main/6.%20The%20Link%20Layer%20and%20LANs)
[![Canva Slides](https://img.shields.io/badge/Canva-slides-7D2AE8?logo=canva&logoColor=white)](#)
[![Notion Lecture](https://img.shields.io/badge/Notion-lecture-37352F?logo=notion&logoColor=white)](https://upbeat-beef-3ff.notion.site/Lecture-slides-The-Link-Layer-and-LANs-2f5915764eda813385b3f4e016324f55?pvs=25)

**Notion laboratory:** [Lab 6.1: Configuring Wireless LAN Access with Cisco Packet Tracer](https://upbeat-beef-3ff.notion.site/Lab-6-1-Configuring-Wireless-LAN-Access-CISCO-Packet-Tracer-2f5915764eda8145a587d75b789f4101?pvs=25)

**Materials:**

- [CSMA simulation and metrics](6.%20The%20Link%20Layer%20and%20LANs)
- [FDMA, TDMA, and 5G scheduling](6.%20The%20Link%20Layer%20and%20LANs)

> **Slides:** Add the Canva presentation link here.

### Unit 7. Wireless and Mobile Networks

**Topics:** Wireless links, Wi-Fi, cellular networks, mobility, wireless channel characteristics, and medium access in wireless environments.

**Chapter:** 7, *Wireless and Mobile Networks*

[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/Networks/tree/main/7.%20Wireless%20and%20Mobile%20Networks)
[![Canva Slides](https://img.shields.io/badge/Canva-slides-7D2AE8?logo=canva&logoColor=white)](#)
[![Notion Lecture](https://img.shields.io/badge/Notion-lecture-37352F?logo=notion&logoColor=white)](https://upbeat-beef-3ff.notion.site/Lecture-slides-Wireless-and-Mobile-Networks-2f5915764eda815586f2fade693aab26?pvs=25)

**Materials:**

- [Wireless networks laboratory](7.%20Wireless%20and%20Mobile%20Networks/wireless_lab.ipynb)
- [Huawei ICT Academy - Yachay Tech](https://upbeat-beef-3ff.notion.site/Huawei-ICT-Academy-Yachay-Tech-2f5915764eda81debde5c7d6a9747d53?pvs=25)

> **Slides:** Add the Canva presentation link here.

### Unit 8. Security in Computer Networks

**Topics:** Threat models, cryptography, authentication, message integrity, firewalls, intrusion detection, and security in practical networked systems.

**Chapter:** 8, *Security in Computer Networks*

[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/Networks/tree/main/8.%20Security%20in%20Computer%20Networks)
[![Canva Slides](https://img.shields.io/badge/Canva-slides-7D2AE8?logo=canva&logoColor=white)](#)
[![Notion Lecture](https://img.shields.io/badge/Notion-lecture-37352F?logo=notion&logoColor=white)](https://upbeat-beef-3ff.notion.site/Lecture-slides-Security-in-Computer-Networks-349915764eda808d8f2ed7e32fe9143c?pvs=25)

**Materials:**

- [Security laboratory](8.%20Security%20in%20Computer%20Networks/security_lab.ipynb)
- [Security CTF laboratory](8.%20Security%20in%20Computer%20Networks/security_lab-CTF.ipynb)
- [Introduction to Cybersecurity](https://www.netacad.com/courses/introduction-to-cybersecurity?courseLang=en-US&instance_id=dea10781-ac0d-41e1-a4df-09d9143fbbe9)

## Assessment

The Notion course plan uses the following weighting:

| Component | Weight | Details |
| --- | ---: | --- |
| Midterm exam | 15% | Covers Units 1-4. |
| Formative evaluation | 50% | Labs 1-8, 6.25% each. |
| Final exam | 15% | Final examination. |
| Final project | 20% | Project presentation and final deliverable. |

## Exams and Project

- [Midterm exam guidelines](https://upbeat-beef-3ff.notion.site/Guidelines-2f5915764eda8166964cf5b9981351c9?pvs=25)
- [Final project presentation: guidelines and rubric](https://upbeat-beef-3ff.notion.site/Guidelines-and-rubric-2f5915764eda811ba9afe9daa272e699?pvs=25)
- [Final exam guidelines](https://upbeat-beef-3ff.notion.site/Guidelines-2f5915764eda81ad8d67dc5d7fd0a8ee?pvs=25)

> **Slides:** Add the Canva presentation link here.

## Books and References

### Main Textbook

- Kurose, J. F., & Ross, K. W. (2025). *Computer Networking: A Top-Down Approach* (9th ed.). Pearson. The chapter sequence and terminology in this repository follow this textbook.

### Supplementary References

- Lakshmanan, V. *Mastering Python Networking*, 4th Edition. Packt.
- Stevens, W. R. (2011). *TCP/IP Illustrated, Volume 1: The Protocols* (2nd ed.). Addison-Wesley.
- Comer, D. E. (2019). *Internetworking with TCP/IP* (6th ed.). Pearson.
- Zybooks. *Introduction to Networking with CompTIA Network+*. zyBooks Interactive Learning.
- Browning, P. (2019). *101 Labs - CompTIA Network+*.
- [Internet Engineering Task Force RFCs](https://www.rfc-editor.org/)
- [Cisco Networking Academy](https://www.netacad.com/)

## Tools

- Python 3.10+
- Jupyter Notebook
- FastAPI and Uvicorn
- Docker
- Git and GitHub
- Wireshark (recommended for packet inspection)

Install the Python dependencies for a specific laboratory using its local setup instructions. When a lab includes a `Dockerfile`, Docker can be used to reproduce the intended environment.

## Other Resources

- [Course resources in Notion](https://upbeat-beef-3ff.notion.site/Resources-2f5915764eda8137b529cf19af30ad1c?pvs=25)
- [Getting started with Docker](https://upbeat-beef-3ff.notion.site/Getting-started-with-Docker-2f5915764eda814a8396c1d685cae19a?pvs=25)
- [Wireshark](https://www.wireshark.org/)
- [Kurose and Ross Wireshark labs](http://gaia.cs.umass.edu/kurose_ross/wireshark.php)
- [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer)

## Repository Structure

```text
.
├── 1. Computer Networks and The Internet/
├── 2. The Application Layer/
│   ├── http-web-server-with-FastAPI/
│   ├── smtp/
│   └── tcp-lab/
├── 3. Transport Layer/
│   ├── auto_testing_scripts/
│   ├── calculator/
│   ├── tcp/
│   ├── threads/
│   └── udp/
├── 4. The Network Layer: Data Plane/
├── 5. The Network Layer: Control Plane/
├── 6. The Link Layer and LANs/
├── 7. Wireless and Mobile Networks/
└── 8. Security in Computer Networks/
```

## Contributing to the Course Materials

When adding a new laboratory or activity:

1. Place it in the unit that covers its main networking concept.
2. Include a short `README.md` with prerequisites and execution steps when needed.
3. Keep examples reproducible and avoid committing passwords, API keys, or personal credentials.
4. Add the activity to the corresponding **Materials** list above.
