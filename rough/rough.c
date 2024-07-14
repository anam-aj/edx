   int b = 0;
            for (int k = 0; k < i - 1; k++)
            {
                if (j == ranks[k])
                {
                    b = 1;
                    break;
                }
            }

            if (b == 1)
            {
                break;
            }

            else if (rank[i] != j)
            {
