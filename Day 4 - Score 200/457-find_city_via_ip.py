"""Based on the text provided from the web page, here is the extracted information regarding the **IP to City Lookup** problem, specifically focusing on the **Python** implementation details, input/output specifications, and thought process.

### Problem Overview
**Title:** IP to City Lookup (华为OD 机试真题)
**Goal:** Given a list of IP address ranges associated with cities and a list of query IPs, determine the "best match" city for each query IP.
**Best Match Definition:** The IP range that contains the query IP and has the **smallest length** (end IP - start IP).

---

### Input & Output Specifications

**Input Format:**
The input consists of exactly **2 lines**:
1.  **Line 1:** A string of city IP ranges separated by semicolons (`;`).
    *   Format per entry: `CityName,StartIP,EndIP` (e.g., `City1,1.1.1.1,2.2.2.2`).
    *   *Note:* The text description says "Start and End separated by comma, multiple ranges by semicolon", but the code logic description implies the format `CityName=StartIP,EndIP` or similar parsing is needed to extract the three components.
    *   Constraints: Up to 500,000 ranges, city names contain letters/numbers/underscores.
2.  **Line 2:** A string of query IPs separated by commas (`,`).
    *   Constraints: Up to 10,000 query IPs.

**Output Format:**
*   A single line containing the matched city names separated by commas (`,`).
*   The length of the output list must match the query IP list.
*   **Critical Rule:** If no match is found for an IP, the output for that position is an empty string, but the **comma separator must still be printed**.
    *   *Example:* If querying `IPa,IPb` and neither matches, the output is `,,` (two empty slots separated by a comma).

---

### Python Thought Process & Logic

The provided text outlines a specific algorithmic approach using Python's `ipaddress` module for efficiency and correctness.

#### 1. IP Conversion
*   **Concept:** Direct string comparison of IPs is unreliable for range checking.
*   **Action:** Use the `ipaddress` module to convert IPv4 addresses into integer representations. This allows for simple numerical comparison (`start <= ip <= end`).

#### 2. Parsing the Input (`parse_ip_ranges`)
*   **Input:** The raw string of city ranges.
*   **Process:**
    *   Split the string by the semicolon (`;`) to get individual city entries.
    *   For each entry, parse the city name, start IP, and end IP.
    *   Convert the start and end IPs to integers.
    *   **Data Structure:** Store this in a dictionary or list of objects where the key is the city name and the value is a list of integer range tuples `(start_int, end_int)`.

#### 3. Finding the Best Match (`find_best_match`)
*   **Input:** A single query IP (converted to integer) and the parsed range data.
*   **Logic:**
    1.  Iterate through all stored city ranges.
    2.  Check if the query IP falls within the range: `if start <= query_ip <= end`.
    3.  If it matches, calculate the **length** of the range: `length = end - start`.
    4.  Compare this length with the current minimum length found so far.
    5.  **Update:** If the new range is smaller (or if it's the first match), update the `best_city` and `min_length`.
    6.  *Note on Overlaps:* The problem states ranges can be nested. By strictly selecting the range with the **minimum length**, we automatically handle the "best match" requirement (e.g., if an IP is in both a large city range and a small specific subnet, the subnet is chosen).

#### 4. Main Execution Flow
1.  Read Line 1 and parse into the `ip_ranges` dictionary.
2.  Read Line 2 and split by comma to get the list of query IPs.
3.  For each query IP:
    *   Convert to integer.
    *   Call `find_best_match`.
    *   Append the result (city name or empty string) to a results list.
4.  Join the results list with commas and print.

---

### Python Code Implementation

Based on the logic described in the text, here is the reconstructed code:

"""
import ipaddress

def ip_to_int(ip_str):
    """Converts an IP string to an integer."""
    return int(ipaddress.IPv4Address(ip_str))

def parse_ip_ranges(ip_range_str):
    """
    Parses the input string into a dictionary.
    Format assumed based on logic: CityName=StartIP,EndIP (separated by semicolons)
    Returns: { 'CityName': [(start_int, end_int), ...] }
    """
    ranges_dict = {}
    # Split by semicolon to get individual city entries
    entries = ip_range_str.split(';')
    
    for entry in entries:
        if not entry.strip():
            continue
            
        # The text implies format like "City1=1.1.1.1,2.2.2.2" or similar
        # We need to split by '=' first to separate city name from IPs
        if '=' in entry:
            city, ip_part = entry.split('=', 1)
            # Split the IP part by comma
            ip_parts = ip_part.split(',')
            if len(ip_parts) == 2:
                start_ip = ip_parts[0].strip()
                end_ip = ip_parts[1].strip()
                
                start_int = ip_to_int(start_ip)
                end_int = ip_to_int(end_ip)
                
                if city not in ranges_dict:
                    ranges_dict[city] = []
                ranges_dict[city].append((start_int, end_int))
                
    return ranges_dict

def find_best_match(query_ip_int, ranges_dict):
    """
    Finds the city with the smallest range containing the query IP.
    """
    best_city = None
    min_range_len = float('inf')
    
    for city, ranges in ranges_dict.items():
        for start, end in ranges:
            if start <= query_ip_int <= end:
                current_len = end - start
                if current_len < min_range_len:
                    min_range_len = current_len
                    best_city = city
                    
    return best_city if best_city else ""

def main():
    try:
        # Read input lines
        # In a real OJ environment, use sys.stdin or input()
        # Assuming input is provided as two lines
        line1 = input().strip()
        line2 = input().strip()
        
        # Parse the IP ranges
        ip_ranges = parse_ip_ranges(line1)
        
        # Parse the query IPs
        query_ips = line2.split(',')
        
        results = []
        for ip_str in query_ips:
            ip_str = ip_str.strip()
            if not ip_str:
                results.append("")
                continue
                
            query_int = ip_to_int(ip_str)
            city = find_best_match(query_int, ip_ranges)
            results.append(city)
            
        # Output results joined by comma
        # Note: If results are ["City1", ""], output is "City1,"
        print(",".join(results))
        
    except EOFError:
        pass

if __name__ == "__main__":
    main()

