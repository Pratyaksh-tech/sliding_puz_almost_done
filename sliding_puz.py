import copy
import sys
sys.setrecursionlimit(20000);

def slide_puzzle(ar):
	orig_ar = copy.deepcopy(ar);
	
	def main(c_ar, orig_ar, depth=1, special=None):
		mt_pos = [];
		childs = [];
		for i in c_ar:
			for j in i:
				if j == 0:
					mt_pos.append(c_ar.index(i));
					mt_pos.append(i.index(j));
		
		if mt_pos[0] != 0:
			childs.append(c_ar[mt_pos[0] - 1][mt_pos[1]]);
		if mt_pos[1] != 0:
			childs.append(c_ar[mt_pos[0]][mt_pos[1] - 1])
		if mt_pos[0] != (len(c_ar) - 1):    
			childs.append(c_ar[mt_pos[0] + 1][mt_pos[1]]);
		if mt_pos[1] != (len(c_ar[mt_pos[1]]) - 1):
			childs.append(c_ar[mt_pos[0]][mt_pos[1] + 1])

		if special != None:
			childs.pop(childs.index(special));
		print(str(childs) + " valuessssssssssssssss")	
		print(str(mt_pos)+" this is the position of 0")	
		def find_comp(o_ar, mt_pos, child, child_pos, depth):
			comp_ar = copy.deepcopy(o_ar);
			
			comp_ar[child_pos[0]][child_pos[1]] = 0;
			comp_ar[mt_pos[0]][mt_pos[1]] = child;			
			
			final_ar = list();
			t = 1
			for k in o_ar:
				temp = list();
				for l in k:
					temp.append(t);
					t+=1;
				final_ar.append(temp);
			final_ar[-1][-1] = 0 	
			
			b = depth;
			h = 0;
			t2 = 0;
			t3 = 0;
			for x in comp_ar:
				t3 = 0
				for y in x:
					if comp_ar[t2][t3] != final_ar[t2][t3]:
						h = h+1;
					t3+=1;	
				t2+=1;
			
			fin_computation = b+h;
			return fin_computation

		static_val = 100000;	
		which_to_move_lst = list();
		print("\n")
		for child in childs:
			child_pos = [];
			for i in c_ar:
				for j in i:
					if j == child:
						#print(str(i.index(j)) + "******")
						#print(str(c_ar.index(i)) + "******66666")
						child_pos.append(c_ar.index(i));
						child_pos.append(i.index(j));			
			computation = find_comp(c_ar, mt_pos, child, child_pos, depth);
			print(str(computation) + " this is statick valueeee" + " this is child " + str(child))
			t_lst2 = list();
			t_lst2.append(child);
			t_lst2.append(computation);
			which_to_move_lst.append(t_lst2);
			
			if computation < static_val:
				static_val = computation;
		
		move_data_lst = [];
		for val in which_to_move_lst:
			if val[-1] == static_val:
				move_data_lst.append(val)

		def move(c_ar, moveto, mt_pos, child_pos2, static_val, orig_ar):
			child_pos = [];
			for i in c_ar:
				for j in i:
					if j == moveto:
						#print(str(i.index(j)) + "******")
						#print(str(c_ar.index(i)) + "******66666")
						child_pos.append(c_ar.index(i));
						child_pos.append(i.index(j));						
			print(str(c_ar) + " before doing")
			final_ar2 = list();
			t2 = 1
			for k2 in c_ar:
				temp2 = list();
				for l2 in k2:
					temp2.append(t2);
					t2+=1;
				final_ar2.append(temp2);
			
			final_ar2[-1][-1] = 0

			c_ar[child_pos[0]][child_pos[1]] = 0;
			print(str(child_pos) + "^^^^^^^^^")
			c_ar[mt_pos[0]][mt_pos[1]] = moveto;
			print(str(c_ar) + " not heeee")
			if c_ar != final_ar2:
				print(str(c_ar)+" 2222222")
				main(c_ar, orig_ar, depth+1, moveto)

			print(str(c_ar) + "heeeeeeeeeeeeeeeeeee")
		move(c_ar, move_data_lst[0][0], mt_pos, child_pos, static_val, orig_ar);	
		
	final_ar = list();
	t = 1
	for k in ar:
		temp = list();
		for l in k:
			temp.append(t);
			t+=1;
		final_ar.append(temp);
	final_ar[-1][-1] = 0 		
	if ar != final_ar:	
		main(ar, orig_ar)

slide_puzzle([[2, 0, 3], [1, 8, 5], [4, 7, 6]])
