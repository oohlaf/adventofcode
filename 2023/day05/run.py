#!/usr/bin/env python3

from pathlib import Path
import re

def parse_data(input):
    """Parse input data."""
    seeds = []
    maps = []
    i = -1
    for line in input.splitlines():
        if line.startswith("seeds:"):
            seeds = list(map(int, list(re.findall(r"\d+", line))))
            continue
        if not len(line):
            continue
        if line[-1] == ':':
            m = re.findall(r"(\w+)-to-(\w+)", line)
            map_src = m[0][0]
            map_dst = m[0][1]
            print("source", map_src, "destination", map_dst)
            i += 1
            maps.append([])
            continue
        m = re.findall(r"(\d+) (\d+) (\d+)", line)
        if m:
            maps[i].append(list(map(int, list(m[0]))))
    return seeds, maps


def translate(i, m):
    dst_start, src_start, length = m
    if src_start <= i < (src_start + length):
        delta = i - src_start
        return (True, dst_start + delta)
    else:
        return (False, i)


def star1(data):
    """Solve puzzle for star 1."""
    seeds, maps = data
    results = []
    for s in seeds:
        dst = s
        for m in maps:
            for t in m:
                done, dst = translate(dst, t)
                if done:
                    break
        results.append(dst)
    print(results)
    return min(results)


def star2_slow(data):
    """Solve puzzle for star 2."""
    seeds, maps = data
    results = []
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        length = seeds[i+1]
        for s in range(start, start + length):
            print("========", s)
            dst = s
            for m in maps:
                print("---", m)
                for t in m:
                    done, dst = translate(dst, t)
                    print(dst)
                    if done:
                        break
            print("result", dst)
            results.append(dst)
    print(results)
    return min(results)


# A  o----o                     o----o
# B        o-------------------o
# every thing else is overlap
def overlap(r, m):
    if r[2]:
        # We already processed this range
        return False
    a_start = r[0]
    a_end = a_start + r[1] - 1
    b_start = m[1]
    b_end = b_start + m[2] - 1
    if a_end < b_start:
        return False
    if a_start > b_end:
        return False
    return True


def intersect(r, m):
    result = []
    a_start = r[0]
    a_end = a_start + r[1] - 1
    b_start = m[1]
    b_end = b_start + m[2] - 1
    i_start = max(a_start, b_start)
    i_end = min(a_end, b_end)
    c_start = m[0]
    length1 = 0
    if a_start < i_start:
        # mark range as unprocessed
        length1 = i_start - a_start
        result.append((a_start, length1, False))
    length2 = i_end - i_start + 1
    # Transform to destination range, mark range as done
    result.append((i_start+c_start-b_start, length2, True))
    length3 = 0
    if a_end > i_end:
        # mark range as unprocessed
        length3 = a_end - i_end
        result.append((i_end+1, length3, False))
    assert length1 + length2 + length3 == r[1]
    return result


def map_range(mapped_ranges, one_map):
    result = []
    # init all ranges as unprocessed for this map
    for r in mapped_ranges:
        result.append((r[0], r[1], False))
    for m in one_map:
        new_result = []
        for r in result:
            if overlap(r, m):
                new_result.extend(intersect(r, m))
            else:
                new_result.append(r)
        result = new_result
    return result


def star2(data):
    """Solve puzzle for star 2."""
    seeds, maps = data
    all_results = []
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        length = seeds[i+1]
        mapped_ranges = [(start, length, False)]
        #print("start range", mapped_ranges)
        for m in maps:
            mapped_ranges = map_range(mapped_ranges, m)
            #print("after map", m, "result", mapped_ranges)
        all_results.extend(mapped_ranges)
    print("results", all_results)
    return min(all_results, key = lambda t: t[0])[0]


def solve(input):
    data = parse_data(input)
    yield star1(data)
    #yield star2_slow(data)
    yield star2(data)


def main():
    input_file = Path(__file__).parent / "input.txt"
    input_text = input_file.read_text().rstrip()
    solutions = solve(input_text)
    print("\n".join(str(s) for s in solutions))


if __name__ == "__main__":
    exit(main())

# 96143715 = too low
