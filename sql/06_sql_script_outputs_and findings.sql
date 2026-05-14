1. The overall summary output:
total_people	avg_charges	  min_charges	max_charges
1338	        13270.420000	1121.87	    63770.43
Findings: The total number of people and rows in the data base is 1338.
Meanings: The average charges amount of the total people is $13,270.42.
          The minimum about of charges of the total people is $1121.87.
          The maximum amount of charges of the total people is $63477.43.

  2. Charges by smoker output:
  smoker	total_people	avg_charges
  1	        274	          32050.230000
  0	        1064	        8434.270000

  Meaning: Charges have much higher insurance costs.

3.  Charges by gender output:
sex	  total_people	avg_charges
male	  676	        13956.750000
female	662	        12569.580000

Meaning: There's not much differnce in charges based on gender

4. Charges by Region output:
region	  total_people	   avg_charges
southeast	   364	           14735.410000
northeast	   324	           13406.380000
northwest	   325	           12417.580000
southwest    325	           12346.940000

Meaning: The southeast region has the highest charges than any other region.

5. children	total_people	avg_charges
   0	          574	        12365.980000
   1	          324        	12731.170000
   2	          240	        15073.560000
   3	          157	        15355.320000
   4	          25	        13850.660000
   5	          18         	8786.040000

Meaning: Insurance charges increases by the number of children

6. Charges based on age output:

age	total_people	avg_charges
18	   69	          7086.220000
19	   68	          9747.910000
20	   29	          10159.700000
21	   28	          4730.460000
22	   28	          10012.930000
23	   28	          12419.820000
24	   28	          10648.020000
25	   28	          9838.360000
26	   28	          6133.830000
27	   28	          12184.700000
28	   28	          9069.190000
29	   27	          10430.160000
30	   27	          12719.110000
31	   27	          10196.980000
32	   26	          9220.300000
33	   26	          12351.530000
34	   26	          11613.530000
35	   25	          11307.180000
36	   25	          12204.480000
37	   25	          18019.910000
38	   25	          8102.730000
39	   25	          11778.240000
40	   27	          11772.250000
41	   27	           9653.740000
42	   27	          13061.040000
43	   27 	        19267.280000
44	   27	          15859.400000
45	   29	          14830.200000
46	   29	          14342.590000
47	   29	          17654.000000
48	   29	          14632.500000
49	   28	          12696.010000
50	   29	          15663.000000
51	   29	          15682.260000
52	   29	          18256.270000
53	   28         	16020.930000
54	   28	          18758.550000
55	   26	          16164.550000
56	   26	          15025.520000
57	   26	          16447.190000
58	   25	          13878.930000
59	   25	          18895.870000
60	   23	          21979.420000
61	   23	          22024.460000
62	   23	          19163.860000
63	   23	          19885.000000
64	   22	          23275.530000

Meaning: Insurance costs graudally inscrease with age.

7. The top ten highest charges output:
age	sex	     bmi	children	smoker	region	   charges
54	female	47.41   	0	      1	    southeast	 63770.43
45	male	  30.36	    0	      1	    southeast	 62592.88
52	male	  34.49	    3	      1	    northwest	 60021.40
31	female	38.10	    1	      1	    northeast	 58571.07
33	female	35.53	    0	      1	    northwest	 55135.40
60	male	  32.80	    0	      1	    southwest	 52590.83
28	male	  36.40	    1	      1	    southwest	 51194.56
64	male	  36.96	    2	      1	    southeast	 49577.66
59	male	  41.14	    1	      1	    southeast	 48970.25
44	female	38.06	    0	      1	    southeast	 48885.14

Meanings and Insights:

--Smoking Status is the number one driver of insurance charges
--Older customers tender to have higher average charges.
--Higher BMI groups often show higher medical insurance costs
--Regional differences exists, but often smaller than smoking differences
--The number of children may affect changes but not as strong as smoking and age.
