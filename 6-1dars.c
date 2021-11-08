#include<stdio.h>
int main()
{

    int son;
    begin:
    printf("oyni kiriting: ");
    scanf("%d",&son);
    switch(son)
    {
        case 1: printf("31 kun\n");break;
        case 2: printf("Yilni kiriting: ");scanf("%d",&son);if(son%4==0 && son%100==0)
        {
            printf("29 kun\n");break;

        }
        else
        {
            printf("28 kun\n");break;
        }
        case 3:printf("31 kun\n");break;
        case 4:printf("31 kun\n");break;
        case 5:printf("31 kun\n");break;
        case 6:printf("31 kun\n");break;
        case 7:printf("31 kun\n");break;
        case 8:printf("31 kun\n");break;
        case 9:printf("31 kun\n");break;
        case 10:printf("31 kun\n");break;
        case 11:printf("31 kun\n");break;
        case 12:printf("31 kun\n");break;
        case 0: goto stop;
        default:
            printf("Bunaqa oy yoq");
    }
    goto begin;
    stop:
    return 0;
}
