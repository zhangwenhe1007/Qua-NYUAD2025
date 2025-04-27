# Qua | قوى

<center>
<img src="https://github.com/zhangwenhe1007/Qua-NYUAD2025/blob/main/images/logo.png">
</center>

## Project Outline

**Qua** is a pioneering project developed during the NYU Quantum Computing Hackathon. The initiative leverages quantum computing technologies to optimize AI training tasks scheduling across GPU clusters in data centers, where traditional methods are extremely energy and cost-inefficient. GPUs are necessary for training AI models in a future where personalized foundational models are critical for various real world tasks.

## Objective
The project aims to optimize the process of distributing AI training jobs across datacenter clusters consisting of CPUs, GPUs, and memory, by using quantum optimization techniques. This approach seeks to reduce AI training energy inefficiencies and increase accessibility to trainable models.

<center>
<img src="https://github.com/zhangwenhe1007/Qua-NYUAD2025/blob/main/images/workflow.png">
</center>

### Data Collection
We utilized a trace dataset for GPU-disaggregated serving of Deep Learning Recommendation Models (DLRMs) from Alibaba Cloud. The dataset captures operational characteristics of 156 inference services, comprising a total of 23,871 inference instances.

Link to dataset github: <a href="https://github.com/alibaba/clusterdata/blob/master/cluster-trace-gpu-v2025/README.md">Alibaba Dataset</a>

### Quantum Computing Application
**Datacenter Job Scheduling Problem**:
   - **Definition**: In datacenters, the job scheduling problem involves the optimal allocation of various computing tasks (AI inference in this project's case) to available computing resources (GPUs, CPUs, Memory) over time. Efficient scheduling is crucial for maximizing the utilization of datacenter hardware, which is a limited resource in small institutions or local communities that use newly custom built datacenters.
   - **Application**: For this project, we applied the Quantum Approximate Optimization Algorithm (QAOA) to solve job scheduling problems. This approach aims to streamline our computational processes, thereby speeding up the analysis of desertification indicators.
   - **Implementation**: We use several different constraints that allow us to schedule AI/ML models inference jobs that require CPUs, GPUs, and memory.
      - Execute as many jobs as possible in any given time over all available machines, ensuring maximum utilization.
      - Every job should be executed exactly once over the entire system.
      - The set of jobs executed on a given machine should not exceed the hardware capacities of that machine.
      - Heavy jobs requiring a lot of computing resources should not be run on the same machine.
      - Repeated submissions of jobs from the same user will decrease the priority of jobs, such as to ensure accessibility of datacenter resources to all users.

<center>
<img src="https://github.com/zhangwenhe1007/Qua-NYUAD2025/blob/main/images/setup.png">
</center>

## Results
The quantum optimization technique is benchmarked against a classical algorithm that assigns jobs per machine by the nearest available machine.

Results show that the quantum optimization technique outperforms the classical algorithm on both the total number of tasks assigned and the number of unique tasks assigned across machines. This highlights quantum technique's potential to reduce model training energy usage and cost by increasing the number of tasks completed at any instant. The applied quantum technique also favors datacenter accessibility by ensuring jobs from different users will be completed if an user overtakes datacenter through multiple job submissions.

We ran the the algorithms on different number of machines from 10 to 100, show below.

<center>
<img src="https://github.com/zhangwenhe1007/Qua-NYUAD2025/blob/main/images/tasknum.png">
</center>

<center>
<img src="https://github.com/zhangwenhe1007/Qua-NYUAD2025/blob/main/images/uniquetasks.png">
</center>









