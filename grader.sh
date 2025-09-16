#!/bin/bash


QUESTION_NUM=$1


if [[ "$QUESTION_NUM" = "q1" ]];
then
    let Q1Grade=$(grep "### Question q1" gradeFile.txt | sed "s/### Question q1: \([0-9]*\)\/15 ###/\1/g")
    if [[ "$Q1Grade" -lt 15 ]];
    then
        exit 5
    fi
    exit 0
fi


if [[ "$QUESTION_NUM" = "q2" ]];
then
    let Q2Grade=$(grep "### Question q2" gradeFile.txt | sed "s/### Question q2: \([0-9]\)\/5 ###/\1/g")
    if [[ "$Q2Grade" -lt 5 ]];
    then
        exit 5
    fi
    exit 0
fi


if [[ "$QUESTION_NUM" = "q3" ]];
then
    let Q3Grade=$(grep "### Question q3" gradeFile.txt | sed "s/### Question q3: \([0-9]*\)\/10 ###/\1/g")
    if [[ "$Q3Grade" -lt 10 ]];
    then
        exit 5
    fi
    exit 0
fi


if [[ "$QUESTION_NUM" = "q4" ]];
then
    let Q4Grade=$(grep "### Question q4" gradeFile.txt | sed "s/### Question q4: \([0-9]*\)\/10 ###/\1/g")
    if [[ "$Q4Grade" -lt 10 ]];
    then
        exit 5
    fi
    exit 0
fi

if [[ "$QUESTION_NUM" = "q5" ]];
then
    let Q5Grade=$(grep "### Question q5" gradeFile.txt | sed "s/### Question q5: \([0-9]*\)\/10 ###/\1/g")
    if [[ "$Q5Grade" -le 10 ]];
    then
        exit 5
    fi
    exit 0
fi
