//+------------------------------------------------------------------+
//|                                                 Modify SL TP.mq4 |
//|                                 Copyright © 2020, FX Masterminds |
//|                                   https://lennykioko.github.io/" |
//+------------------------------------------------------------------+
#property copyright "Copyright � 2020, FX Masterminds."
#property link      "https://lennykioko.github.io/"

//version 1.0

//show input parameter
#property show_inputs


enum e_type{
 pips=1,
 price=2,
};

input e_type  type = pips;

extern double sl = 0;
extern double tp = 0;
extern string comment = "";


double Poin;
//+------------------------------------------------------------------+
//| Custom initialization function                                   |
//+------------------------------------------------------------------+
int init() {

   if (Point == 0.00001) Poin = 0.0001;
   else {
      if (Point == 0.001) Poin = 0.01;
      else Poin = Point;
   }
   return(0);
}

//+------------------------------------------------------------------+
//| script program start function                                    |
//+------------------------------------------------------------------+

int start() {
   if (type == 1) {
      ModifyPips();
   }
   if (type == 2) {
      ModifyPrice();
   }
   return(0);
}

int ModifyPips() {
//----
   int ordertotal = OrdersTotal();
   for (int i=0; i<ordertotal; i++)
   {
      int order = OrderSelect(i, SELECT_BY_POS, MODE_TRADES);
      if (OrderSymbol() == Symbol())
         if (OrderComment() == comment && OrderType()==OP_BUY || OrderType()==OP_BUYSTOP)
         {
            int ticket = OrderModify(OrderTicket(), OrderOpenPrice(), OrderOpenPrice()-sl*Poin, OrderOpenPrice()+tp*Poin, 0);
         }

         if (OrderComment() == comment && OrderType()==OP_SELL || OrderType()==OP_SELLSTOP)
         {
            int ticket2 = OrderModify(OrderTicket(), OrderOpenPrice(), OrderOpenPrice()+sl*Poin, OrderOpenPrice()-tp*Poin, 0);
         }
      }
//----
return(0);
}


int ModifyPrice() {
//----
   int ordertotal = OrdersTotal();
   for (int i=0; i<ordertotal; i++)
   {
      int order = OrderSelect(i, SELECT_BY_POS, MODE_TRADES);
      if (OrderSymbol() == Symbol())
         if (OrderComment() == comment)
         {
            OrderModify(OrderTicket(), OrderOpenPrice(), sl, tp, 0);
         }
      }
//----
return(0);
}
//+------------------------------------------------------------------+
