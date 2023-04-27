public class Order {
    private int orderId;
    private LocalDate orderDate;
    private LocalDate deliveryDate;
    private Customer customer;
    private List<OrderItem> orderItems;
    private BigDecimal totalPrice;
    private BigDecimal tax;
    private BigDecimal discount;
    private Address shippingAddress;
    private boolean inStock;

    // constructor and getters/setters omitted for brevity

    public void cancelOrder() {
        // cancel the order
    }

    public void returnOrder() {
        // process a return for the order
    }

    public void updateOrder() {
        // update various fields in the order
    }

    public OrderSummary getSummary() {
        return new OrderSummary(orderId, totalPrice, tax, discount);
    }
}

public class OrderSummary {
    private int orderId;
    private BigDecimal totalPrice;
    private BigDecimal tax;
    private BigDecimal discount;

    public OrderSummary(int orderId, BigDecimal totalPrice, BigDecimal tax, BigDecimal discount) {
        this.orderId = orderId;
        this.totalPrice = totalPrice;
        this.tax = tax;
        this.discount = discount;
    }

    public int getOrderId() {
        return orderId;
    }

    public BigDecimal getTotalPrice() {
        return totalPrice;
    }

    public BigDecimal getTax() {
        return tax;
    }

    public BigDecimal getDiscount() {
        return discount;
    }
}
