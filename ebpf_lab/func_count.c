#include <linux/bpf.h>
#include <linux/version.h>
#include <linux/ptrace.h>
#include <linux/sched.h>
#include <linux/fs.h>
#include <linux/types.h>

#define FUNC_NAME "vfs_read"

struct bpf_map_def {
    __u32 type;
    __u32 key_size;
    __u32 value_size;
    __u32 max_entries;
};

struct bpf_map_def func_count = {
    .type = BPF_MAP_TYPE_HASH,
    .key_size = sizeof(__u64),
    .value_size = sizeof(__u64),
    .max_entries = 1,
};

// Declaration of bpf_map_lookup_elem() and bpf_map_update_elem()
void *bpf_map_lookup_elem(void *map, const void *key);
int bpf_map_update_elem(void *map, const void *key, const void *value, __u64 flags);

int bpf_func_count(struct pt_regs *ctx) {
    __u64 zero = 0, *val;
    val = bpf_map_lookup_elem(&func_count, &zero);
    if (val)
        (*val)++;
    else
        bpf_map_update_elem(&func_count, &zero, &zero, BPF_ANY);
    return 0;
}

char _license[] = "GPL";
