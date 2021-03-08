//
//  main.cpp
//  DataStructure
//
//  Created by YURUN LI on 2021/01/01.
//

#include <iostream>
# define MaxSize 10
using namespace std;

typedef struct LNode{
    int data;
    struct LNode *next;
}LNode, *LinkList;

//初始化

//带头结点插入
bool ListInsert(LinkList &L, int i, int e){
    if (i<1) {
        return false;
    }
    LNode *p;
    p = L;
    int j=0; //p指向的是第几个节点
    while(p!=NULL && j<i-1){
        p=p->next;
        j++;
    }
    if (p==NULL) {
        return false;
    }
    LNode *s =(LNode *)malloc(sizeof(LNode));
    s->data = e;
    s->next = p->next;
    p->next = s;
    return true;
}
//不带头结点插入
bool ListInsertN(LinkList &L,int i, int e){
    if (i<1) { //指向第一个节点之前 error
        return false;
    }
    if (i ==1) { //指向第一个节点, 与后续节点不同情况处理
        LNode *s = (LNode *)malloc(sizeof(LNode));
        s->data = e;
        s->next = L;
        L = s;
        return true;
    }
    LNode *p;  // 指向第二个节点及之后的情况
    int j=1;
    p = L;
    while (p!=NULL && j< i-1) { //将p指向第i个节点a[i-1]
        p = p->next;
        j++;
    }
    if (p==NULL) { //如果i值超出节点范围
        return false;
    }
    //节点a[i-1]指向s, s指向节点a[i]
    LNode *s = (LNode *)malloc(sizeof(LNode));
    s->next = p->next;
    s->data = e;
    p->next = s;
    return true; //插入成功
}
//指定节点的后插操作 O(1)
bool InsertNextNode(LNode *p, int e){
    if (p==NULL) {
        return false;
    }
    LNode *s = (LNode *)malloc(sizeof(LNode));
    if (s==NULL) {
        return false; //内存分配失败
    }
    s->data = e;
    s->next = p->next;
    p->next = s;
    return true;
}
//指定节点的前插操作 O(1)
bool InsertPriorNode(LNode *p, int e){
    if (p == NULL) {
        return false;
    }
    LNode *s = (LNode *)malloc(sizeof(LNode));
    if (s == NULL) {
        return false;
    }
    s->data = p->data;
    s->next = p->next;
    p->data = e;
    p->next = s;
    return true;
}
//按位序删除 O(n)
bool ListDelete(LinkList &L, int i, int &e){
    if (i<1) {
        return false;
    }
    LNode *p;
    int j=0;
    p = L;
    while (p!=NULL && j<i-1) {
        p = p->next;
        j++;
    }
    if (p == NULL) {
        return false;
    }
    if (p->next == NULL) {
        return false;
    }
    LNode *q = p->next;
    p->next = q->next;
    e = q->data;
    free(q);
    return true;
}
//删除指定节点 O(1)
bool DeleteNode(LNode *p){
    if (p == NULL) {
        return false;
    }
    LNode *q = p->next;
    p->data = q->next->data;
    p->next = q->next;
    free(q);
    return true;
}
///按位查找
///(带头节点)
//按位查找 O(n)
LNode *GetElem(LinkList L, int i){
    if (i<0) {
        return NULL;
    }
    LNode *p;
    int j=0;
    p = L;
    while (p!=NULL && j<i) {
        p = p->next;
        j++;
    }
    return p;
}
//按值查找 O(n)
LNode *LocateElem(LinkList L, int e){
    LNode *p = L->next;
    while (p!=NULL || p->data != e) {
        p = p->next;
    }
    return p; //找到后返回该节点指针,或者没找到返回NULL
}
//求表长 O(n)
int LinkListLength(LinkList L){
    int len = 0;
    LNode *p =L;
    while (p->next != NULL) {
        len++;
        p = p->next;
    }
    return len;
}
///单链表的创建///
//尾插法
LinkList List_TailInsert(LinkList &L){
    int x;
    L=(LinkList)malloc(sizeof(LNode));
    LNode *s,*r = L;
    scanf("%d",&x);
    while (x!=9999) {
        s=(LNode *)malloc(sizeof(LNode));
        s->data =x;
        r->next =s;
        r = s;
        scanf("%d",&x);
    }
    r->next = NULL;
    return L;
}
//头插法

//int main(){
//    LinkList L=List_TailInsert(L);
//    LNode *p=L->next;
//    while (p!= NULL) {
//        cout << p->data <<" ";
//        p = p->next;
//    }
//    cout << endl;
//    int len = LinkListLength(L);
//    cout << "表长为:"<< len <<endl;
//    int e;
//    ListDelete(L, 5, e);
//    cout<< "删除元素为:"<<e<<endl;
//    p=L->next;
//    while (p!= NULL) {
//        cout << p->data <<" ";
//        p = p->next;
//    }
//    cout << endl;
//    return 0;
//}
#include <sstream>
#include <iostream>

using namespace std;

int main(){
    int a;
    float b;
    istringstream istr;
    istr.str("5.68");
    cout << istr.str() << endl;
    istr >> a;
    cout << a << endl;
    istr >> b;
    cout << b << endl;
    return 0;
}
