class solutions:
     def longest_commom_prefix(self, strs: list[str]) -> str:
          if not strs:
            return ""
          
          prefix = strs[0]
          for i in strs[1:]:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:                    
                    return ""
          return prefix

sol = solutions()
print(sol.longest_commom_prefix(['chetan', 'chaitali', 'chirag']))