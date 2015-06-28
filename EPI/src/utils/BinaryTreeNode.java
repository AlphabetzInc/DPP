package utils;

import java.util.*;

import static java.lang.Math.abs;
import static java.lang.Math.max;

/**
 * Created by Pankaj on 6/12/15.
 */
public class BinaryTreeNode {
    private int _val;
    private BinaryTreeNode _left;
    private BinaryTreeNode _right;

    public BinaryTreeNode(int val, BinaryTreeNode left, BinaryTreeNode right)
    {
        this._val = val;
        this._left = left;
        this._right = right;
    }

    public int val() { return _val; }

    public BinaryTreeNode left() {
        return _left;
    }

    public BinaryTreeNode right() {
        return _right;
    }

    public boolean isLeaf(){
        return left() == null && right() == null;
    }

    public int height(){
        int h = 0;
        if(isLeaf())
            return 0;
        if (left() != null)
            h = left().height();
        if (right() != null && right().height() > h)
            h = right().height();
        return 1+h;
    }

    public boolean isBalancedSlow(){
        if(left() == null && right() == null){
            return true;
        }
        else if(left() == null){
            return right().height() <= 1;
        }
        else if(right() == null){
            return left().height() <= 1;
        }
        else{
            boolean res;
            res = Math.abs(left().height() - right().height()) <= 1;
            res &= left().isBalancedSlow();
            res &= right().isBalancedSlow();
            return res;
        }
    }

    public boolean isBalanced(){
        return heightBalanced() != -2;
    }

    private int heightBalanced() {
        if(isLeaf()) return 0;
        int l_height, r_height;
        l_height = left() == null ? -1 : left().heightBalanced();
        if(l_height == -2) return -2;
        r_height = right() == null ? -1 : right().heightBalanced();
        if(r_height == -2) return -2;
        if(abs(l_height - r_height) > 1) return -2;
        return 1 + max(l_height,r_height);
    }

    public List<Integer> inOrder()
    {
        List<Integer> vals = new ArrayList<Integer>();
        if(this.left() != null)
            vals.addAll(this.left().inOrder());
        vals.add(this.val());
        if(this.right() != null)
            vals.addAll(this.right().inOrder());
        return vals;
    }

    //TODO: implement morris traversal
    public List<Integer> inOrderMorris()
    {
        return inOrder();
    }

    public List<Integer> preOrder()
    {
        List<Integer> vals = new ArrayList<Integer>();
        vals.add(this.val());
        if(this.left() != null)
            vals.addAll(this.left().preOrder());
        if(this.right() != null)
            vals.addAll(this.right().preOrder());
        return vals;
    }

    public List<Integer> postOrder()
    {
        List<Integer> vals = new ArrayList<Integer>();
        if(this.left() != null)
            vals.addAll(this.left().postOrder());
        if(this.right() != null)
            vals.addAll(this.right().postOrder());
        vals.add(this.val());
        return vals;
    }

    public List<Integer> levelOrder()
    {
        List<Integer> vals = new ArrayList<Integer>();
        Queue<BinaryTreeNode> q = new LinkedList<BinaryTreeNode>();
        q.add(this);
        while(!q.isEmpty())
        {
            BinaryTreeNode node = q.remove();
            vals.add(node.val());
            if(node.left() != null)
                q.add(node.left());
            if(node.right() != null)
                q.add(node.right());
        }
        return vals;
    }

    /**
     * @return List of list of nodes at each level by depth
     */
    public List<List<Integer>> levelOrderByDepth()
    {
        List<List<Integer>> ls = new ArrayList<List<Integer>>();
        Queue<BinaryTreeNode> q = new LinkedList<BinaryTreeNode>();
        q.add(this);
        int numNodesCurrLevel = 0, numNodesPrevLevel = 0;
        numNodesPrevLevel ++;
        while(!q.isEmpty())
        {
            List<Integer> currDepth = new ArrayList<Integer>();
            while(numNodesPrevLevel > 0 && !q.isEmpty())
            {
                BinaryTreeNode node = q.remove();
                numNodesPrevLevel--;
                currDepth.add(node.val());
                if(node.left() != null){
                    q.add(node.left());
                    numNodesCurrLevel++;
                }
                if(node.right() != null){
                    q.add(node.right());
                    numNodesCurrLevel++;
                }
            }
            numNodesPrevLevel = numNodesCurrLevel;
            numNodesCurrLevel = 0;
            ls.add(currDepth);
        }
        return ls;
    }
}

