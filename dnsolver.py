import sys
import dns.resolver as resolv
from typing import Generator, Union




def dnsolver(domain_name: str) -> Union[Generator[str, str, None], None]:
    '''
        Returns information about domain names
    '''
    qtypes = ['A', 'AAAA', 'MX', 'NS', 'TXT', 'SOA']

    for qtype in qtypes:
        res = resolv.query(domain_name, qtype, raise_on_no_answer=False)
        if res.rrset is not None:
            yield res.rrset
        else:
            return None


if __name__ == '__main__':

    print("****** DNSOLVER 1.0 ********\n")
    print("****** made by Carlos ********\n")

    if len(sys.argv) > 1:
        domain_name = str(sys.argv[1])
    else:
        domain_name = str(input("Enter the domain name you want to analyze: \n"))
    try:
        for i in dnsolver(domain_name):
            print(i)
    except Exception as e:
        print(f"Exception: {e} ")
    finally:
        print("Goodbye!")
        sys.exit()



