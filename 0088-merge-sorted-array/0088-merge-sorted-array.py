class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # so voi so nam cuoi chuoi
        p1 = m - 1 
        p2 = n - 1
        p = m + n - 1
        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]: 
                # so cuoi chuoi 1 (truoc so 0) > so cuoi chuoi 2 -> vi hai so nay la lon nhat chuoi 1 va 2 nen
                # nums1[p1] lon nhat -> ve cuoi chuoi
                nums1[p] = nums1[p1]

                #Lui lai de so sanh so lon thu 2 cua nums1 va so lon nhat nums2 - lap lien tuc het chuoi
                p1 -= 1
            else:
                #nguoc lai thi nums2[p2] lon hon
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1