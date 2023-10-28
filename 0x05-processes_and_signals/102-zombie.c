#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - main function
 *
 * Return: 0
 */
int main(void)
{
	pid_t pid;
	int n = 0;

	while (n < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			n++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (0);
}

/**
 * infinite_while - sub function
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
