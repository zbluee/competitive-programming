class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_domains = defaultdict(int)

        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            domain = domain.split(".")
            for i in range(len(domain)):
                parent_domain = ".".join(domain[i:])
                count_domains[parent_domain] += int(count)

        return [f'{count} {domain}' for domain, count in count_domains.items()]


        
