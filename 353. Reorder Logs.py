def reorder_logs(logs):
    def key(log):
        id_, rest = log.split(" ", 1)
        return (0, rest, id_) if rest[0].isalpha() else (1,)
    
    return sorted(logs, key=key)

# Example Usage
logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog"]
print(reorder_logs(logs))
# Output: ["g1 act car", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]