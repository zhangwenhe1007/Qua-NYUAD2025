import pandas as pd

def greedy_scheduler(csv_file, num_machines=30, cap_cpu=256, cap_gpu=8, cap_memory=1024, job_limit=2000):
    """
    Greedy First-Come-First-Serve Job Scheduler.

    Parameters:
    - csv_file (str): Path to the CSV file with job data.
    - num_machines (int): Number of machines in the cluster.
    - cap_cpu, cap_gpu, cap_memory (int): Resource capacities per machine.
    - job_limit (int): Number of jobs to process from the dataset.

    Returns:
    - machines_assignment_fcfs (list): List of machine job assignment summaries.
    - total_tasks_fcfs (int): Total number of jobs assigned.
    """

    # Load dataset
    df = pd.read_csv(csv_file)
    subset_df = df.head(job_limit).copy()
    subset_df_sorted = subset_df.sort_values(by=['app_name', 'creation_time'])

    # Initialize machines
    machines_refined = [{
        'id': f'machine_{j}',
        'remaining_cpu': cap_cpu,
        'remaining_gpu': cap_gpu,
        'remaining_memory': cap_memory,
        'assigned_jobs': []
    } for j in range(num_machines)]

    # Greedy assignment
    for _, row in subset_df_sorted.iterrows():
        for machine in machines_refined:
            if (row['cpu_request'] <= machine['remaining_cpu'] and
                row['gpu_request'] <= machine['remaining_gpu'] and
                row['memory_request'] <= machine['remaining_memory']):

                machine['remaining_cpu'] -= row['cpu_request']
                machine['remaining_gpu'] -= row['gpu_request']
                machine['remaining_memory'] -= row['memory_request']
                machine['assigned_jobs'].append({
                    'instance_sn': row['instance_sn'],
                    'app_name': row['app_name'],
                    'estimated_runtime': row['estimated_runtime'],
                    'cpu_request': row['cpu_request'],
                    'gpu_request': row['gpu_request'],
                    'memory_request': row['memory_request']
                })
                break  # Move to next job once assigned

    # Prepare summary
    machines_assignment_fcfs = [{
        'machine_id': m['id'],
        'num_jobs': len(m['assigned_jobs']),
        'assigned_job_ids': [job['instance_sn'] for job in m['assigned_jobs']],
        'remaining_cpu': m['remaining_cpu'],
        'remaining_gpu': m['remaining_gpu'],
        'remaining_memory': m['remaining_memory'],
        'total_runtime': sum(job['estimated_runtime'] for job in m['assigned_jobs'])
    } for m in machines_refined]

    total_tasks_fcfs = sum(len(m['assigned_jobs']) for m in machines_refined)

    return machines_assignment_fcfs, total_tasks_fcfs

# Example usage
if __name__ == "__main__":
    summary, total = greedy_scheduler("filtered_DLRM_trace.csv")
    print(f"Total tasks scheduled: {total}")
    for machine in summary:
        print(machine)
